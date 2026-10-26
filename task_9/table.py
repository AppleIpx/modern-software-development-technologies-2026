from common.numbers import is_odd


def row_sums(matrix):
    """Суммы строк. Для [] возвращает []. Матрица не изменяется."""
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums


def column_sums(matrix):
    """Суммы столбцов прямоугольной матрицы. Для [] возвращает []."""
    if not matrix:
        return []
    sums = [0] * len(matrix[0])
    for row in matrix:
        for column, value in enumerate(row):
            sums[column] += value
    return sums


def diagonal_pattern(size):
    """Квадратная таблица size × size: 0 на главной диагонали, 1 выше неё, 2 ниже."""
    pattern = []
    for row in range(size):
        line = []
        for column in range(size):
            if row == column:
                line.append(0)
            elif row < column:
                line.append(1)
            else:
                line.append(2)
        pattern.append(line)
    return pattern


def transform(matrix):
    """Вариант 4: новая матрица той же формы, нечётные элементы заменены нулями.

    Исходная матрица не изменяется; для [] возвращает [].
    """
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if is_odd(value):
                new_row.append(0)
            else:
                new_row.append(value)
        result.append(new_row)
    return result
