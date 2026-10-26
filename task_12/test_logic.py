import copy

from task_12.logic import (
    add_record,
    delete_record,
    find_by_id,
    find_records,
    next_id,
    set_completed,
    sorted_by_id,
    statistics,
    validate_records,
)


def make(record_id, title, category, amount, completed=False):
    return {"id": record_id, "title": title, "category": category, "amount": amount, "completed": completed}


def expect_value_error(function, *args):
    try:
        function(*args)
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"


# --- Проверка записей
validate_records([])
validate_records([make(1, "Бег", "кардио", 30), {**make(2, "Йога", "гибкость", 0), "extra": 1}])
expect_value_error(validate_records, {"id": 1})  # не список
expect_value_error(validate_records, [5])  # не словарь
expect_value_error(validate_records, [{"id": 1, "title": "a", "category": "b", "amount": 1}])  # нет ключа
expect_value_error(validate_records, [make(True, "a", "b", 1)])  # id=bool
expect_value_error(validate_records, [make(0, "a", "b", 1)])
expect_value_error(validate_records, [make(1, "a", "b", True)])  # amount=bool
expect_value_error(validate_records, [make(1, "a", "b", -1)])
expect_value_error(validate_records, [make(1, "a", "b", 1.5)])
expect_value_error(validate_records, [make(1, "  ", "b", 1)])
expect_value_error(validate_records, [make(1, "a", "", 1)])
expect_value_error(validate_records, [make(1, "a", "b", 1, "false")])  # completed не bool
expect_value_error(validate_records, [make(1, "a", "b", 1), make(1, "c", "d", 2)])  # повторный id

# --- Добавление: id, очистка пробелов, начальный статус, одинаковые названия
records = []
assert next_id(records) == 1
first = add_record(records, "  Python  ", " кардио ", 4)
assert first == {"id": 1, "title": "Python", "category": "кардио", "amount": 4, "completed": False}
second = add_record(records, "Python", "кардио", 2)  # одинаковые названия разрешены
assert second["id"] == 2 and len(records) == 2
expect_value_error(add_record, records, "", "x", 1)
expect_value_error(add_record, records, "x", "x", -1)
assert len(records) == 2  # лишней записи нет

# --- Поиск без учёта регистра
assert find_records(records, "PY") == records
assert find_records(records, "нет такого") == []
expect_value_error(find_records, records, "   ")
assert find_records([], "x") == []

# --- Статус
assert set_completed(records, 2, True) is True and records[1]["completed"] is True
assert set_completed(records, 2, False) is True and records[1]["completed"] is False
before = copy.deepcopy(records)
assert set_completed(records, 99, True) is False
assert records == before  # неизвестный id данных не меняет

# --- Удаление: id остальных не меняются, новый id = max + 1
records = [make(1, "A", "x", 1), make(2, "B", "x", 2)]
assert delete_record(records, 1) is True
assert [record["id"] for record in records] == [2]
assert next_id(records) == 3
assert delete_record(records, 1) is False
assert len(records) == 1
assert find_by_id(records, 2)["title"] == "B" and find_by_id(records, 1) is None

# --- Порядок по id
unordered = [make(3, "C", "x", 1), make(1, "A", "x", 1)]
assert [record["id"] for record in sorted_by_id(unordered)] == [1, 3]
assert [record["id"] for record in unordered] == [3, 1]  # исходный не изменён

# --- Статистика: пустой список, два статуса, две категории
empty_stats = statistics([])
assert empty_stats == {"total": 0, "done": 0, "not_done": 0, "amount_sum": 0, "by_category": {}}
data = [make(1, "A", "кардио", 4, False), make(2, "B", "силовая", 2, True), make(3, "C", " кардио ", 3, True)]
saved = copy.deepcopy(data)
stats = statistics(data)
assert stats["total"] == 3 and stats["done"] == 2 and stats["not_done"] == 1
assert stats["amount_sum"] == 9
assert stats["by_category"] == {"кардио": 7, "силовая": 2}  # пробелы по краям убраны
assert data == saved  # статистика данные не меняет
two = statistics([make(1, "A", "x", 4), make(2, "B", "y", 2, True)])
assert two["total"] == 2 and two["done"] == 1 and two["not_done"] == 1 and two["amount_sum"] == 6

print("Все проверки пройдены")
