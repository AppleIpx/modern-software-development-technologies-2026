# Вариант 4: нечётные числа (в Python -3 % 2 == 1, так что условие верно и для отрицательных).
n = int(input("Сколько чисел (n >= 0): "))

count = 0
total = 0
for index in range(n):
    number = int(input(f"Число {index + 1}: "))
    if number % 2 != 0:
        count += 1
        total += number

print(f"Количество нечётных: {count}")
print(f"Сумма нечётных: {total}")
