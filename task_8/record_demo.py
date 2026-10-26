# Задание 3: запись как словарь и пара как кортеж.
record = {"title": "Python", "hours": 4}
print("Запись:", record)

record["hours"] = 6  # замена значения по существующему ключу
record["completed"] = False  # новый ключ
print("После изменения:", record)

pair = (record["title"], record["hours"])
title, hours = pair  # распаковка кортежа
print(f"Пара: {title}, {hours}")
