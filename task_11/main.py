import json
import sys
from pathlib import Path

from common.console import read_non_negative_int, read_positive_int
from common.jsonio import read_json, write_json
from task_11.analysis import (
    completion_counts,
    leaders_tasks,
    select_tasks,
    top_users,
    validate_todos,
)

FOLDER = Path(__file__).resolve().parent


def load_todos(path):
    """Прочитать и проверить todos.json. Исключения передаются вызывающему коду."""
    data = read_json(path)
    validate_todos(data)
    return data


def load_safely(path):
    """Вернуть (данные, None) или (None, сообщение об ошибке)."""
    try:
        return load_todos(path), None
    except FileNotFoundError:
        return None, f"файл не найден: {path}"
    except UnicodeError:
        return None, "файл не в кодировке UTF-8"
    except json.JSONDecodeError as error:  # раньше ValueError: это его подкласс
        return None, f"некорректный JSON: {error}"
    except ValueError as error:
        return None, f"ошибка структуры: {error}"
    except OSError as error:
        return None, f"ошибка доступа к файлу: {error}"


def analyze(todos, user_id, threshold):
    counts = completion_counts(todos)
    leaders = top_users(counts)
    return {
        "counts": counts,
        "leaders": leaders,
        "leaders_tasks": leaders_tasks(todos, leaders),
        "selected": select_tasks(todos, user_id, threshold),
    }


def save_results(folder, result):
    write_json(Path(folder) / "leaders.json", result["leaders_tasks"])
    write_json(Path(folder) / "selected.json", result["selected"])


def run_analysis(todos_path, out_folder, user_id, threshold):
    """Загрузить, проверить, посчитать и только потом записать результаты. Ошибки — исключениями."""
    todos = load_todos(todos_path)
    result = analyze(todos, user_id, threshold)
    save_results(out_folder, result)
    return result


def main():
    todos, error = load_safely(FOLDER / "todos.json")
    if error is not None:
        print(f"Ошибка: {error}. Прежние результаты не изменены.")
        return 1

    counts = completion_counts(todos)
    print("Выполнено задач по пользователям:")
    for user_id in sorted(counts):
        print(f"  пользователь {user_id}: {counts[user_id]}")
    leaders = top_users(counts)
    print("Лидеры: " + (", ".join(str(user_id) for user_id in leaders) if leaders else "нет"))

    user_id = read_positive_int("userId для отбора задач: ")
    threshold = read_non_negative_int("Порог (отбираются задачи с id больше порога): ")
    result = analyze(todos, user_id, threshold)
    print(f"Задачи лидеров (id): {[todo['id'] for todo in result['leaders_tasks']]}")
    print(f"Отобрано для пользователя {user_id} (id): {[todo['id'] for todo in result['selected']]}")

    try:
        save_results(FOLDER, result)
    except OSError as error:
        print(f"Ошибка записи результатов: {error}")
        return 1
    print("Сохранено: leaders.json, selected.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
