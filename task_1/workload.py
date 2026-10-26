first_subject = input("Название первого предмета: ")
first_lessons = int(input(f"Занятий по предмету «{first_subject}» в неделю: "))
first_duration = int(input("Продолжительность одного занятия, мин: "))

second_subject = input("Название второго предмета: ")
second_lessons = int(input(f"Занятий по предмету «{second_subject}» в неделю: "))
second_duration = int(input("Продолжительность одного занятия, мин: "))

available_hours = float(input("Доступное время на неделю, ч: "))

first_minutes = first_lessons * first_duration
second_minutes = second_lessons * second_duration
total_minutes = first_minutes + second_minutes
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

print()
print(f"{first_subject}: {first_minutes} мин")
print(f"{second_subject}: {second_minutes} мин")
print(f"Общая нагрузка: {total_minutes} мин ({total_hours:.2f} ч)")
print(f"Свободное время: {free_hours:.2f} ч")
print(f"Нагрузка за четыре недели: {four_weeks_hours:.2f} ч")
