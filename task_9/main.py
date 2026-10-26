from task_9.table import column_sums, diagonal_pattern, row_sums, transform


def read_matrix():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    matrix = read_matrix()
    print(f"Суммы строк: {row_sums(matrix)}")
    print(f"Суммы столбцов: {column_sums(matrix)}")

    print("Исходная таблица:")
    print_matrix(matrix)
    print("После преобразования (нечётные → 0):")
    print_matrix(transform(matrix))

    size = int(input("Размер диагонального узора (>= 1): "))
    print_matrix(diagonal_pattern(size))


if __name__ == "__main__":
    main()
