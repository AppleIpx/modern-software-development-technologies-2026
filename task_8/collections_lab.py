PUNCTUATION = ".,!?;:"

# Вариант 4: спортивные тренировки, amount — минуты. Три категории, «кардио» повторяется.
TRAININGS = [
    {"title": "Бег утром", "category": "кардио", "amount": 30},
    {"title": "Плавание", "category": "кардио", "amount": 45},
    {"title": "Приседания", "category": "силовая", "amount": 20},
    {"title": "Жим лёжа", "category": "силовая", "amount": 25},
    {"title": "Растяжка", "category": "гибкость", "amount": 15},
    {"title": "Велосипед", "category": "кардио", "amount": 60},
]


def word_counts(text):
    """Вернуть словарь «слово → количество»: нижний регистр, без .,!?;: по краям слов."""
    counts = {}
    for word in text.split():
        cleaned = word.strip(PUNCTUATION).lower()
        if cleaned == "":
            continue
        counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_word_counts(counts):
    """Вывести пары «слово: количество» по алфавиту."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Отсортированный список тем, общих для двух списков."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Отсортированный список всех уникальных тем двух списков."""
    return sorted(set(first) | set(second))


def totals_by_category(records):
    """Словарь «категория → сумма amount». Входные записи не изменяются."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    """Названия записей категории в исходном порядке; неизвестная категория → []."""
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles


def sorted_totals(records):
    """Дополнительно: пары (категория, сумма) по убыванию суммы, затем по названию категории."""
    totals = totals_by_category(records)
    return sorted(totals.items(), key=lambda pair: (-pair[1], pair[0]))


def main():
    text = input("Текст для подсчёта слов: ")
    print_word_counts(word_counts(text))

    print()
    print("Сводка по категориям (минуты):")
    totals = totals_by_category(TRAININGS)
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")

    print()
    category = input("Категория для поиска: ")
    print(f"Тренировки категории «{category}»: {titles_in_category(TRAININGS, category)}")

    print()
    print(f"По убыванию суммы: {sorted_totals(TRAININGS)}")


if __name__ == "__main__":
    main()
