first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print(f"До обмена: первая — {first_room}, вторая — {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print(f"После обмена: первая — {first_room}, вторая — {second_room}")
