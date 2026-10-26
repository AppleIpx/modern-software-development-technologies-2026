numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

# Новый список: отрицательные заменены модулями, исходный не меняется.
result = []
for number in numbers:
    if number < 0:
        result.append(-number)
    else:
        result.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {result}")
