import csv

from common.numbers import is_odd


def _parse_ints(line, line_number, expected_count, what):
    parts = line.split()
    if len(parts) != expected_count:
        raise ValueError(f"Строка {line_number}: ожидалось {expected_count} {what}, найдено {len(parts)}")
    try:
        return [int(part) for part in parts]
    except ValueError:
        raise ValueError(f"Строка {line_number}: найдено не целое число") from None


def read_matrix(path):
    """Прочитать матрицу из UTF-8 файла.

    Формат: первая строка — «строки столбцы» (положительные целые), далее ровно столько строк,
    сколько указано, в каждой ровно столько целых, сколько указано. Один перевод строки после
    последней строки допустим; лишние и пустые строки — ошибка.
    Raises ValueError при ошибке формата, FileNotFoundError / OSError / UnicodeError при ошибках чтения.
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        text = file.read()

    lines = [line.rstrip("\r") for line in text.split("\n")]
    if lines and lines[-1] == "":
        lines.pop()  # допустим один перевод строки в конце
    if not lines:
        raise ValueError("Файл пуст")

    rows, columns = _parse_ints(lines[0], 1, 2, "чисел в заголовке")
    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: размеры должны быть положительными")

    data_lines = lines[1:]
    if len(data_lines) < rows:
        raise ValueError(f"Ожидалось строк данных: {rows}, найдено: {len(data_lines)}")
    if len(data_lines) > rows:
        raise ValueError(f"Строка {rows + 2}: лишняя строка данных")

    matrix = []
    for offset, line in enumerate(data_lines):
        line_number = offset + 2
        if line.strip() == "":
            raise ValueError(f"Строка {line_number}: пустая строка")
        matrix.append(_parse_ints(line, line_number, columns, "чисел"))
    return matrix


def selected_sum(matrix):
    """Вариант 4: сумма нечётных элементов матрицы (нет подходящих — 0)."""
    total = 0
    for row in matrix:
        for value in row:
            if is_odd(value):
                total += value
    return total


def export_csv(matrix, path):
    """Дополнительно: записать матрицу в CSV стандартным модулем csv."""
    with open(path, "w", encoding="utf-8", newline="") as file:
        csv.writer(file).writerows(matrix)
