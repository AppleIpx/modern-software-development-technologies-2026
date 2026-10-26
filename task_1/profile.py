last_name = input("Фамилия: ")
first_name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет): "))
favorite_subject = input("Любимый предмет: ")
study_hours = float(input("Часов подготовки в неделю: "))

full_name = f"{first_name} {last_name}"
age_in_four_years = age + 4
hours_four_weeks = study_hours * 4
hours_per_day = study_hours / 7

print()
print("=== Карточка студента ===")
print(f"Полное имя: {full_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Возраст через четыре года: {age_in_four_years}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Подготовка в неделю: {study_hours:.2f} ч")
print(f"Подготовка за четыре недели: {hours_four_weeks:.2f} ч")
print(f"Подготовка в день (в среднем): {hours_per_day:.2f} ч")
