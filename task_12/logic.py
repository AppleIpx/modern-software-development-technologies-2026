"""Логика проекта «План тренировок» (вариант 4): без ввода-вывода и файлов.

amount — продолжительность в минутах, completed — «тренировка завершена».
"""

REQUIRED_KEYS = ("id", "title", "category", "amount", "completed")


def _is_int(value):
    # type(...) is int отсекает bool: True проходит isinstance(value, int), но числом считаться не должно.
    return type(value) is int


def validate_records(records):
    """Проверить весь набор записей. Ничего не изменяет; при нарушении — ValueError с пояснением."""
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком")
    seen_ids = set()
    for index, record in enumerate(records):
        place = f"Запись {index + 1}"
        if not isinstance(record, dict):
            raise ValueError(f"{place}: запись должна быть объектом")
        for key in REQUIRED_KEYS:
            if key not in record:
                raise ValueError(f"{place}: нет поля {key}")
        if not _is_int(record["id"]) or record["id"] <= 0:
            raise ValueError(f"{place}: id должен быть положительным целым")
        if record["id"] in seen_ids:
            raise ValueError(f"{place}: повторяющийся id {record['id']}")
        seen_ids.add(record["id"])
        for key in ("title", "category"):
            if not isinstance(record[key], str) or record[key].strip() == "":
                raise ValueError(f"{place}: {key} должно быть непустой строкой")
        if not _is_int(record["amount"]) or record["amount"] < 0:
            raise ValueError(f"{place}: amount должен быть целым числом не меньше нуля")
        if type(record["completed"]) is not bool:
            raise ValueError(f"{place}: completed должно быть логическим значением")


def next_id(records):
    """Идентификатор для новой записи: max + 1, для пустого списка — 1."""
    return max((record["id"] for record in records), default=0) + 1


def add_record(records, title, category, amount):
    """Добавить запись В КОНЕЦ списка records (список изменяется) и вернуть её.

    Название и категория очищаются от краевых пробелов; completed = False.
    Выбрасывает ValueError, если данные некорректны (список в этом случае не меняется).
    """
    title = title.strip() if isinstance(title, str) else title
    category = category.strip() if isinstance(category, str) else category
    record = {"id": next_id(records), "title": title, "category": category,
              "amount": amount, "completed": False}
    validate_records([record])
    records.append(record)
    return record


def find_by_id(records, record_id):
    """Вернуть запись с таким id или None. Список не изменяется."""
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def find_records(records, query):
    """Записи, в названии которых есть подстрока query (без учёта регистра), в исходном порядке.

    Пустой запрос отклоняется (ValueError). Список не изменяется.
    """
    query = query.strip()
    if query == "":
        raise ValueError("Поисковый запрос не должен быть пустым")
    lowered = query.lower()
    return [record for record in records if lowered in record["title"].lower()]


def set_completed(records, record_id, completed):
    """Установить статус записи. Список изменяется. True при успехе, False — если id неизвестен."""
    record = find_by_id(records, record_id)
    if record is None:
        return False
    record["completed"] = completed
    return True


def delete_record(records, record_id):
    """Удалить запись по id. Список изменяется, остальные id не меняются.

    True при успехе, False — если id неизвестен.
    """
    record = find_by_id(records, record_id)
    if record is None:
        return False
    records.remove(record)
    return True


def sorted_by_id(records):
    """Новый список записей по возрастанию id (исходный список не изменяется)."""
    return sorted(records, key=lambda record: record["id"])


def statistics(records):
    """Статистика по списку: total, done, not_done, amount_sum, by_category (категория → сумма).

    Категории сравниваются точно после удаления краевых пробелов. Список не изменяется.
    """
    by_category = {}
    done = 0
    amount_sum = 0
    for record in records:
        category = record["category"].strip()
        by_category[category] = by_category.get(category, 0) + record["amount"]
        amount_sum += record["amount"]
        if record["completed"]:
            done += 1
    return {
        "total": len(records),
        "done": done,
        "not_done": len(records) - done,
        "amount_sum": amount_sum,
        "by_category": by_category,
    }
