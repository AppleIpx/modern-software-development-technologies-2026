numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if not numbers:
    print("Нет данных")
else:
    print(f"Количество: {len(numbers)}")
    print(f"Сумма: {sum(numbers)}")
    print(f"Минимум: {min(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Среднее: {sum(numbers) / len(numbers):.2f}")
