# Вариант 4: заказ «Художественная мастерская», позиции «Альбомы» и «Наборы кистей».
order_name = input("Название заказа: ")
customer = input("Имя заказчика: ")

first_name = input("Название первой позиции: ")
first_quantity = int(input("Количество: "))
first_price = float(input("Цена единицы, руб.: "))

second_name = input("Название второй позиции: ")
second_quantity = int(input("Количество: "))
second_price = float(input("Цена единицы, руб.: "))

delivery = float(input("Стоимость доставки, руб.: "))
paid = float(input("Внесённая сумма, руб.: "))

first_cost = first_quantity * first_price
second_cost = second_quantity * second_price
goods_cost = first_cost + second_cost
total = goods_cost + delivery
total_quantity = first_quantity + second_quantity
change = paid - total

print()
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer}")
print(f"{first_name} | {first_quantity} | {first_price:.2f} | {first_cost:.2f}")
print(f"{second_name} | {second_quantity} | {second_price:.2f} | {second_cost:.2f}")
print(f"Стоимость товаров: {goods_cost:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итого с доставкой: {total:.2f} руб.")
print(f"Всего единиц: {total_quantity}")
print(f"Внесено: {paid:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
