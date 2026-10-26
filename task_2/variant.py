# Вариант 4: общий объём — количество деталей, вместимость единицы — деталей в контейнере.
total = int(input("Количество деталей (целое, >= 0): "))
capacity = int(input("Деталей в контейнере (целое, > 0): "))

full_containers = total // capacity
remainder = total % capacity
min_containers = (total + capacity - 1) // capacity

print(f"Полностью заполненных контейнеров: {full_containers}")
print(f"Остаток деталей: {remainder}")
print(f"Минимум контейнеров для всех деталей: {min_containers}")
