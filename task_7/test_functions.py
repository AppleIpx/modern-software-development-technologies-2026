from task_7.functions import average, is_palindrome, normalize_text, select_numbers, sum_digits

# Базовые проверки
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# Вариант 4: числа не меньше порога
assert select_numbers([-5, 0, 2, 5], 2) == [2, 5]
assert select_numbers([], 2) == []
assert select_numbers([-5, 0, 1], 2) == []  # пустая выборка
assert select_numbers([1, 2, 3], 2) == [2, 3]  # граница включена
assert select_numbers([1, 2, 3], 3) == [3]
assert select_numbers([3, 1, 3, 2, 3], 3) == [3, 3, 3]  # повторы сохраняются
assert select_numbers([-5, 0, 2, 5], 0) == [0, 2, 5]  # порог 0
source = [-5, 0, 2, 5]
saved_copy = source.copy()
select_numbers(source, 2)
assert source == saved_copy  # исходный список не изменён
assert average(source) == 0.5 and source == saved_copy

# Дополнительно: is_palindrome (проверки написаны до реализации)
assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("Python") is False
assert is_palindrome("") is False
assert is_palindrome("     ") is False
assert is_palindrome("а") is True
assert is_palindrome("А!") is False

print("Базовые проверки пройдены")
