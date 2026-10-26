from common.validation import is_positive_int, is_strict_bool


def validate_todos(data):
    """Проверить структуру списка задач; при нарушении выбросить ValueError с пояснением."""
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком")
    seen_ids = set()
    for index, todo in enumerate(data):
        place = f"Запись {index + 1}"
        if not isinstance(todo, dict):
            raise ValueError(f"{place}: запись должна быть объектом")
        for key in ("id", "userId", "title", "completed"):
            if key not in todo:
                raise ValueError(f"{place}: нет поля {key}")
        if not is_positive_int(todo["id"]):
            raise ValueError(f"{place}: id должен быть положительным целым")
        if not is_positive_int(todo["userId"]):
            raise ValueError(f"{place}: userId должен быть положительным целым")
        if not isinstance(todo["title"], str) or todo["title"].strip() == "":
            raise ValueError(f"{place}: title должен быть непустой строкой")
        if not is_strict_bool(todo["completed"]):
            raise ValueError(f"{place}: completed должно быть логическим значением")
        if todo["id"] in seen_ids:
            raise ValueError(f"{place}: повторяющийся id {todo['id']}")
        seen_ids.add(todo["id"])


def completion_counts(todos):
    """Словарь «userId → число выполненных задач» для всех пользователей набора (включая 0)."""
    counts = {}
    for todo in todos:
        user_id = todo["userId"]
        counts[user_id] = counts.get(user_id, 0)
        if todo["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):
    """Отсортированный список пользователей с максимумом выполненных задач; для {} и максимума 0 — []."""
    if not counts:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    return sorted(user_id for user_id, count in counts.items() if count == maximum)


def leaders_tasks(todos, leaders):
    """Завершённые задачи лидеров в исходном порядке."""
    return [todo for todo in todos if todo["completed"] and todo["userId"] in leaders]


def select_tasks(todos, user_id, parameter=None):
    """Вариант 4: задачи пользователя user_id, у которых id больше порога parameter.

    Порядок записей сохраняется, исходные записи не изменяются.
    Для неизвестного пользователя результат — [].
    """
    if parameter is None:
        raise ValueError("Для варианта 4 нужен числовой порог")
    return [todo for todo in todos if todo["userId"] == user_id and todo["id"] > parameter]
