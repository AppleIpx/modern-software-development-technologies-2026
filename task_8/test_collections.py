from task_8.collections_lab import (
    TRAININGS,
    all_topics,
    common_topics,
    sorted_totals,
    titles_in_category,
    totals_by_category,
    word_counts,
)

# Частоты слов
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}

# Темы
first = ["python", "sql", "python"]
second = ["sql", "git"]
assert common_topics(first, second) == ["sql"]
assert all_topics(first, second) == ["git", "python", "sql"]
assert common_topics([], second) == []
assert all_topics([], second) == ["git", "sql"]

# Общий набор из условия
records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
saved = [record.copy() for record in records]
assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}
assert records == saved  # исходные записи не изменены

# Собственный набор варианта 4 (тренировки)
saved_trainings = [record.copy() for record in TRAININGS]
assert totals_by_category(TRAININGS) == {"кардио": 135, "силовая": 45, "гибкость": 15}
assert titles_in_category(TRAININGS, "кардио") == ["Бег утром", "Плавание", "Велосипед"]
assert titles_in_category(TRAININGS, "гибкость") == ["Растяжка"]
assert titles_in_category(TRAININGS, "йога") == []
assert TRAININGS == saved_trainings

# Дополнительно: сортировка пар
assert sorted_totals(TRAININGS) == [("кардио", 135), ("силовая", 45), ("гибкость", 15)]
tie = [
    {"title": "x", "category": "б", "amount": 5},
    {"title": "y", "category": "а", "amount": 5},
]
assert sorted_totals(tie) == [("а", 5), ("б", 5)]  # при равных суммах — по названию
assert sorted_totals([]) == []

print("Все проверки пройдены")
