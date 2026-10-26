import contextlib
import csv
import io
from pathlib import Path
from tempfile import TemporaryDirectory

from task_10.files_lab import export_csv, read_matrix, selected_sum
from task_10.main import main


def expect_value_error(path, fragment=None):
    try:
        read_matrix(path)
    except ValueError as error:
        if fragment is not None:
            assert fragment in str(error), str(error)
    else:
        assert False, "Ошибка не обнаружена"


def run_main(*args):
    with contextlib.redirect_stdout(io.StringIO()) as output:
        code = main([str(arg) for arg in args])
    return code, output.getvalue()


with TemporaryDirectory() as directory:
    folder = Path(directory)
    path = folder / "matrix.txt"

    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

    path.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
    assert read_matrix(path) == [[1, -2, 3], [4, 0, -6]]

    path.write_text("2 3\n1 -2 3\n4 0 -6", encoding="utf-8")  # без конечного перевода строки
    assert read_matrix(path) == [[1, -2, 3], [4, 0, -6]]

    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]

    path.write_text("", encoding="utf-8")
    expect_value_error(path)

    path.write_text("0 3\n", encoding="utf-8")
    expect_value_error(path)

    path.write_text("1 2\n1\n", encoding="utf-8")
    expect_value_error(path, "Строка 2")

    path.write_text("1 2\n1 x\n", encoding="utf-8")
    expect_value_error(path, "Строка 2")

    path.write_text("1 1\n5\n6\n", encoding="utf-8")
    expect_value_error(path)

    path.write_text("2 1\n5\n", encoding="utf-8")  # строк данных меньше заголовка
    expect_value_error(path)

    path.write_text("1 1\n5\n\n", encoding="utf-8")  # лишняя пустая строка
    expect_value_error(path)

    path.write_text("a b\n", encoding="utf-8")  # нечисловой заголовок
    expect_value_error(path, "Строка 1")

    try:
        read_matrix(folder / "нет_такого.txt")
    except FileNotFoundError:
        pass
    else:
        assert False, "Ошибка не обнаружена"

    # Вариант 4: сумма нечётных
    assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 4
    assert selected_sum([[2, 4]]) == 0
    assert selected_sum([[7]]) == 7  # 1×1 — элемент учитывается один раз
    assert selected_sum([[-3, -5]]) == -8

    # Основная программа: отчёт записывается после успешной проверки
    path.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
    report = folder / "report.txt"
    code, _ = run_main(path, report)
    assert code == 0
    assert report.read_text(encoding="utf-8") == (
        "Суммы строк: 2 -2\nСуммы столбцов: 5 -2 -3\nРезультат варианта: 4\n"
    )

    # Некорректный вход не трогает существующий отчёт и сам не изменяется
    old_report = report.read_text(encoding="utf-8")
    bad_input = folder / "bad.txt"
    bad_input.write_text("2 2\n1 2\n", encoding="utf-8")
    bad_before = bad_input.read_bytes()
    code, output = run_main(bad_input, report)
    assert code == 1 and "Ошибка формата" in output
    assert report.read_text(encoding="utf-8") == old_report
    assert bad_input.read_bytes() == bad_before

    code, output = run_main(folder / "нет_такого.txt", report)
    assert code == 1 and "не найден" in output
    assert report.read_text(encoding="utf-8") == old_report

    bad_input.write_bytes(b"\xff\xfe\x00")  # не UTF-8
    code, output = run_main(bad_input, report)
    assert code == 1 and "UTF-8" in output
    assert report.read_text(encoding="utf-8") == old_report

    # CSV
    csv_path = folder / "matrix.csv"
    export_csv([[1, -2, 3], [4, 0, -6]], csv_path)
    with open(csv_path, encoding="utf-8", newline="") as file:
        assert list(csv.reader(file)) == [["1", "-2", "3"], ["4", "0", "-6"]]

print("Все проверки пройдены")
