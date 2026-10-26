def _read_int(prompt, is_valid, too_small_message):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Ошибка: не целое число")
            continue
        if not is_valid(number):
            print(too_small_message)
            continue
        return number


def read_positive_int(prompt):
    """Повторять ввод, пока не получено целое число больше нуля."""
    return _read_int(prompt, lambda number: number > 0, "Ошибка: число должно быть больше нуля")


def read_non_negative_int(prompt):
    """Повторять ввод, пока не получено целое число не меньше нуля."""
    return _read_int(prompt, lambda number: number >= 0, "Ошибка: число не может быть отрицательным")
