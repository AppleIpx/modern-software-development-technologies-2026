import sys
from pathlib import Path

from common.console import read_positive_int
from task_10.files_lab import read_matrix, selected_sum
from task_9.table import column_sums, row_sums

FOLDER = Path(__file__).resolve().parent


def read_positive_integer():
    """Повторять ввод, пока не получено целое число больше нуля."""
    return read_positive_int("Положительное целое число: ")


def build_report(matrix):
    return (
        "Суммы строк: " + " ".join(str(value) for value in row_sums(matrix)) + "\n"
        "Суммы столбцов: " + " ".join(str(value) for value in column_sums(matrix)) + "\n"
        f"Результат варианта: {selected_sum(matrix)}\n"
    )


def main(argv=None):
    """Прочитать матрицу, проверить её и только затем записать отчёт. Возвращает код выхода."""
    args = sys.argv[1:] if argv is None else argv
    matrix_path = Path(args[0]) if len(args) > 0 else FOLDER / "matrix.txt"
    report_path = Path(args[1]) if len(args) > 1 else FOLDER / "report.txt"

    try:
        matrix = read_matrix(matrix_path)
        report = build_report(matrix)  # всё проверено и посчитано до открытия отчёта на запись
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {matrix_path}")
        return 1
    except UnicodeError:  # раньше ValueError: UnicodeDecodeError — его подкласс
        print("Ошибка: файл не в кодировке UTF-8")
        return 1
    except ValueError as error:
        print(f"Ошибка формата: {error}")
        return 1
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return 1

    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write(report)
    except OSError as error:
        print(f"Ошибка записи отчёта: {error}")
        return 1

    print(report, end="")
    print(f"Отчёт сохранён: {report_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
