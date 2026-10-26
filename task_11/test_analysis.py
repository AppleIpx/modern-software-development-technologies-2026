import copy
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from task_11.analysis import (
    completion_counts,
    leaders_tasks,
    select_tasks,
    top_users,
    validate_todos,
)
from common.jsonio import write_json
from task_11.main import load_safely, run_analysis

TODOS = json.loads(Path(__file__).with_name("todos.json").read_text(encoding="utf-8"))


def ids(tasks):
    return [task["id"] for task in tasks]


def expect_value_error(data):
    try:
        validate_todos(data)
    except ValueError:
        pass
    else:
        assert False, f"Ошибка не обнаружена: {data!r}"


# Учебный набор
validate_todos(TODOS)
counts = completion_counts(TODOS)
assert counts == {5: 2, 10: 2}
assert top_users(counts) == [5, 10]
assert ids(leaders_tasks(TODOS, top_users(counts))) == [1, 3, 4, 5]

# Пустой набор и набор без выполненных
assert completion_counts([]) == {}
assert top_users({}) == []
only_open = [{"id": 1, "userId": 7, "title": "x", "completed": False}]
assert completion_counts(only_open) == {7: 0}  # пользователь с нулём присутствует
assert top_users(completion_counts(only_open)) == []
assert leaders_tasks(only_open, top_users(completion_counts(only_open))) == []

# Один лидер и несколько
assert top_users({5: 3, 10: 1}) == [5]
assert top_users({10: 2, 5: 2, 7: 1}) == [5, 10]

# Вариант 4: id больше порога
saved = copy.deepcopy(TODOS)
assert ids(select_tasks(TODOS, 5, 2)) == [5]
assert TODOS == saved  # исходные записи не изменены
assert select_tasks(TODOS, 999, 2) == []  # неизвестный пользователь
assert select_tasks(TODOS, 5, 5) == []  # непустой набор без совпадений
assert ids(select_tasks(TODOS, 5, 1)) == [2, 5]  # граница: id == порогу не входит
assert ids(select_tasks(TODOS, 5, 0)) == [1, 2, 5]  # порог 0
assert select_tasks([], 5, 0) == []
try:
    select_tasks(TODOS, 5)
except ValueError:
    pass
else:
    assert False, "Параметр обязателен"

# Ошибки структуры
expect_value_error({"id": 1})  # вместо списка объект
expect_value_error([{"id": 1, "userId": 5, "title": "a", "completed": True},
                    {"id": 1, "userId": 5, "title": "b", "completed": False}])  # повторный id
expect_value_error([{"id": 1, "title": "a", "completed": True}])  # нет userId
expect_value_error([{"id": 1, "userId": 5, "title": "a", "completed": "false"}])
expect_value_error([{"id": True, "userId": 5, "title": "a", "completed": True}])
expect_value_error([{"id": 1, "userId": 5, "title": "  ", "completed": True}])
expect_value_error([{"id": 0, "userId": 5, "title": "a", "completed": True}])
expect_value_error([42])
validate_todos([{"id": 1, "userId": 5, "title": "a", "completed": True, "extra": 1}])  # доп. ключи допустимы

with TemporaryDirectory() as directory:
    folder = Path(directory)
    todos_path = folder / "todos.json"
    write_json(todos_path, TODOS)

    # Запись и повторное чтение JSON
    result = run_analysis(todos_path, folder, 5, 2)
    reread = json.loads((folder / "selected.json").read_text(encoding="utf-8"))
    assert reread == result["selected"] == select_tasks(TODOS, 5, 2)
    leaders_reread = json.loads((folder / "leaders.json").read_text(encoding="utf-8"))
    assert ids(leaders_reread) == [1, 3, 4, 5]

    # Ошибки входа: сообщение есть, прежние результаты не перезаписаны
    leaders_before = (folder / "leaders.json").read_bytes()
    selected_before = (folder / "selected.json").read_bytes()

    todos_path.write_text("{не json", encoding="utf-8")
    data, error = load_safely(todos_path)
    assert data is None and "JSON" in error
    todos_path.write_bytes(b"\xff\xfe\x00")
    data, error = load_safely(todos_path)
    assert data is None and "UTF-8" in error
    todos_path.write_text('{"id": 1}', encoding="utf-8")
    data, error = load_safely(todos_path)
    assert data is None and "структуры" in error
    data, error = load_safely(folder / "нет_файла.json")
    assert data is None and "не найден" in error

    for broken in ("{не json", '{"id": 1}'):
        todos_path.write_text(broken, encoding="utf-8")
        try:
            run_analysis(todos_path, folder, 5, 2)
        except ValueError:
            pass
        else:
            assert False, "Ошибка не обнаружена"
    assert (folder / "leaders.json").read_bytes() == leaders_before
    assert (folder / "selected.json").read_bytes() == selected_before

print("Все проверки пройдены")
