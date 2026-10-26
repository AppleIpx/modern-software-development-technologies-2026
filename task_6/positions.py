numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if not numbers:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for index, number in enumerate(numbers):
        if number == maximum:
            positions.append(index)
    print(f"Индексы максимума: {positions}")
