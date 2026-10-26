"""Консольное меню проекта «План тренировок» (вариант 4)."""
import json
import sys
from pathlib import Path

from task_12.logic import (
    add_record,
    delete_record,
    find_by_id,
    find_records,
    set_completed,
    sorted_by_id,
    statistics,
)
from task_12.storage import load_records, save_records

DEFAULT_PATH = Path(__file__).resolve().parent / "data.json"

MENU = """
=== План тренировок ===
1. Показать записи
2. Добавить запись
3. Найти записи
4. Изменить статус
5. Удалить запись
6. Показать статистику
7. Сохранить данные
8. Выйти"""


def format_record(record):
    status = "завершена" if record["completed"] else "не завершена"
    return (f"{record['id']} | {record['title']} | {record['category']} | "
            f"{record['amount']} мин | {status}")


def ask_non_empty(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Ошибка: значение не должно быть пустым")


def ask_amount(prompt):
    while True:
        text = input(prompt).strip()
        try:
            amount = int(text)
        except ValueError:
            print("Ошибка: нужно целое число")
            continue
        if amount < 0:
            print("Ошибка: число не может быть отрицательным")
            continue
        return amount


def ask_id(prompt):
    """Вернуть целый id или None, если введено не целое число."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Ошибка: id должен быть целым числом")
        return None


def show_records(records):
    if not records:
        print("Нет записей")
        return
    for record in sorted_by_id(records):
        print(format_record(record))


def add_action(records):
    title = ask_non_empty("Название тренировки: ")
    category = ask_non_empty("Категория: ")
    amount = ask_amount("Продолжительность, мин: ")
    record = add_record(records, title, category, amount)
    print(f"Добавлено: {format_record(record)}")


def find_action(records):
    query = input("Подстрока названия: ").strip()
    if not query:
        print("Ошибка: поисковый запрос не должен быть пустым")
        return
    found = find_records(records, query)
    if not found:
        print("Ничего не найдено")
        return
    for record in found:
        print(format_record(record))


def status_action(records):
    record_id = ask_id("ID записи: ")
    if record_id is None:
        return
    if find_by_id(records, record_id) is None:
        print("Запись с таким ID не найдена")
        return
    while True:
        answer = input("Новый статус (1 — завершена, 0 — не завершена): ").strip()
        if answer in ("0", "1"):
            break
        print("Ошибка: введите 1 или 0")
    set_completed(records, record_id, answer == "1")
    print("Статус изменён")


def delete_action(records):
    record_id = ask_id("ID записи: ")
    if record_id is None:
        return
    if find_by_id(records, record_id) is None:
        print("Запись с таким ID не найдена")
        return
    if input("Удалить запись? (да — подтвердить): ").strip().lower() != "да":
        print("Удаление отменено")
        return
    delete_record(records, record_id)
    print("Запись удалена")


def statistics_action(records):
    stats = statistics(records)
    print(f"Всего записей: {stats['total']}")
    print(f"Завершено: {stats['done']}")
    print(f"Не завершено: {stats['not_done']}")
    print(f"Суммарная продолжительность: {stats['amount_sum']} мин")
    for category in sorted(stats["by_category"]):
        print(f"  {category}: {stats['by_category'][category]} мин")


def save_action(records, path):
    """Вернуть True, если данные сохранены; сообщение об успехе — только после успешной записи."""
    try:
        save_records(path, records)
    except (OSError, ValueError) as error:
        print(f"Ошибка сохранения: {error}")
        return False
    print(f"Данные сохранены: {Path(path).name}")
    return True


def exit_action(records, path):
    """Вернуть True, если можно завершать программу."""
    while True:
        answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
        if answer == "да":
            return save_action(records, path)  # при ошибке остаёмся в меню
        if answer == "нет":
            return True
        print("Ответьте «да» или «нет»")


def load_on_start(path):
    """Вернуть (записи, None) или (None, причина). Отсутствие файла — пустой список."""
    try:
        return load_records(path), None
    except FileNotFoundError:
        print(f"Файл {Path(path).name} не найден: начинаем с пустого списка")
        return [], None
    except UnicodeError:  # раньше ValueError: UnicodeDecodeError — его подкласс
        return None, "файл не в кодировке UTF-8"
    except json.JSONDecodeError as error:  # раньше ValueError: это его подкласс
        return None, f"повреждённый JSON: {error}"
    except ValueError as error:
        return None, f"неправильная структура данных: {error}"
    except OSError as error:
        return None, f"ошибка доступа к файлу: {error}"


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    path = Path(args[0]) if args else DEFAULT_PATH

    records, error = load_on_start(path)
    if error is not None:
        print(f"Запуск прекращён: {error}. Файл не изменён.")
        return 1

    actions = {
        "1": show_records,
        "2": add_action,
        "3": find_action,
        "4": status_action,
        "5": delete_action,
        "6": statistics_action,
    }
    while True:
        print(MENU)
        command = input("Команда: ").strip()
        if command in actions:
            actions[command](records)
        elif command == "7":
            save_action(records, path)
        elif command == "8":
            if exit_action(records, path):
                return 0
        else:
            print("Неизвестная команда, повторите выбор")


if __name__ == "__main__":
    sys.exit(main())
