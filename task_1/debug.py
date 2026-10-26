# Фрагмент А
# Ожидание: сумма 5. Причина ошибки: "2" и "3" — строки, + их соединяет ("23").
first = "2"
second = "3"
print("А. Типы до преобразования:", type(first), type(second))
first_number = int(first)
second_number = int(second)
print("А. Типы после преобразования:", type(first_number), type(second_number))
print("А. Сумма:", first_number + second_number)

# Фрагмент Б
# Ожидание: возраст через год, 18. Причина ошибки: input() возвращает str,
# а str + int вызывает TypeError. Ввод для проверки — 17.
age = input("Б. Возраст: ")
print("Б. Тип до преобразования:", type(age))
age = int(age)
print("Б. Тип после преобразования:", type(age))
print("Б. Возраст через год:", age + 1)

# Фрагмент В
# Ожидание: среднее 7.0. Причина ошибки: деление выполняется раньше сложения,
# поэтому считалось 4 + 7 + (10 / 3). Нужны скобки.
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("В. Среднее:", average)
