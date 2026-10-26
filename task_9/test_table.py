from task_9.table import column_sums, diagonal_pattern, row_sums, transform

assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

# Вариант 4: нечётные заменить нулями
source = [[-2, 0, 3], [4, -5, 6]]
saved = [row.copy() for row in source]
result = transform(source)
assert result == [[-2, 0, 0], [4, 0, 6]]
assert source == saved  # исходная матрица не изменена
result[0][0] = 100
assert source == saved  # строки результата независимы от исходных
assert transform([[1, 3], [5, 7]]) == [[0, 0], [0, 0]]  # все нечётные
assert transform([[2, 4]]) == [[2, 4]]  # нет нечётных
assert transform([[-1]]) == [[0]]  # отрицательное нечётное

# Функции не меняют полученную матрицу
matrix = [[1, 2, 3], [4, 5, 6]]
row_sums(matrix)
column_sums(matrix)
assert matrix == [[1, 2, 3], [4, 5, 6]]

print("Все проверки пройдены")
