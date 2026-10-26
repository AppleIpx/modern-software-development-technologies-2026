from task_7.functions import average, normalize_text, select_numbers, sum_digits


def read_numbers():
    return [int(part) for part in input("Целые числа через пробел: ").split()]


def main():
    number = int(input("Целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    numbers = read_numbers()
    mean = average(numbers)
    if mean is None:
        print("Нет данных")
    else:
        print(f"Среднее: {mean:.2f}")

    text = input("Произвольный текст: ")
    print(f"Нормализованный текст: {normalize_text(text)!r}")

    threshold = int(input("Порог (целое, >= 0): "))
    print(f"Числа не меньше порога {threshold}: {select_numbers(numbers, threshold)}")


if __name__ == "__main__":
    main()
