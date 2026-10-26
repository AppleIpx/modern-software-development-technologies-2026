def sum_digits(number):
    """Вернуть сумму цифр модуля целого числа (для 0 — 0)."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def average(numbers):
    """Вернуть среднее списка чисел или None для пустого списка. Список не меняется."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Вернуть текст в нижнем регистре без краевых пробелов и с одним пробелом между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вариант 4: вернуть новый список чисел, не меньших порога (порядок и повторы сохраняются).

    Исходный список не изменяется.
    """
    result = []
    for number in numbers:
        if number >= threshold:
            result.append(number)
    return result


def is_palindrome(text):
    """Дополнительно: палиндром по правилам работы №5 (регистр и обычные пробелы игнорируются).

    Для пустого нормализованного текста возвращает False.
    """
    cleaned = text.lower().replace(" ", "")
    if cleaned == "":
        return False
    return cleaned == cleaned[::-1]
