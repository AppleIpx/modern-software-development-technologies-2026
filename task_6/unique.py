# Дополнительно: удалить повторы с сохранением порядка первого появления, без set.
numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

result = []
for number in numbers:
    if number not in result:
        result.append(number)

print(f"Исходный список: {numbers}")
print(f"Без повторов: {result}")
