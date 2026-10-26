text = input("Введите текст: ")

replacements = text.count(":")
new_text = text.replace(":", "-")

print(f"Замен: {replacements}")
print(f"Новая строка: {new_text}")
