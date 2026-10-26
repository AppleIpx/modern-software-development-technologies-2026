text = input("Введите текст: ")

# Игнорируем регистр и обычные пробелы; остальные символы сравниваем как есть.
cleaned = text.lower().replace(" ", "")

if cleaned == "":
    print("Нет текста")
elif cleaned == cleaned[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
