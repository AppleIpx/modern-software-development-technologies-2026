rejected = 0
number = int(input("Введите положительное целое: "))
while number <= 0:
    rejected += 1
    number = int(input("Нужно положительное. Повторите ввод: "))

print(f"Квадрат: {number ** 2}")
print(f"Отклонено попыток: {rejected}")
