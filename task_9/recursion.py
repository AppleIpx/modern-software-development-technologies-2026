# Дополнительно: рекурсия. Факториал рекурсивно и итеративно, трассировка factorial(3).


def factorial(number, depth=0, trace=False):
    """Аргумент — целое число от 0 до 20."""
    if trace:
        print("  " * depth + f"вызов factorial({number})")
    if number == 0:
        if trace:
            print("  " * depth + "возврат 1")
        return 1
    result = number * factorial(number - 1, depth + 1, trace)
    if trace:
        print("  " * depth + f"возврат {result}")
    return result


def factorial_iterative(number):
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def main():
    assert factorial(0) == 1
    assert factorial(5) == 120
    print("Трассировка factorial(3):")
    factorial(3, trace=True)
    for number in range(21):
        assert factorial(number) == factorial_iterative(number), number
    print("Рекурсивная и итеративная версии совпали для чисел 0–20")


if __name__ == "__main__":
    main()
