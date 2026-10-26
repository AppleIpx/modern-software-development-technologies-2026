# Вариант 4: слова, начинающиеся с «к».
text = input("Введите строку: ")

matches = []
for word in text.split():
    cleaned = word.strip(".,!?;:").lower()
    if cleaned == "":
        continue
    if cleaned.startswith("к"):
        matches.append(cleaned)

if matches:
    for word in matches:
        print(word)
else:
    print("Нет совпадений")
print(f"Количество: {len(matches)}")
