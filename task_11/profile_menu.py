# Дополнительно: выбор источника профиля — сеть или локальный пример — с общей функцией вывода.
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError

from common.jsonio import read_json
from task_11.fetch_profile import fetch_profile

SAMPLE_PATH = Path(__file__).resolve().parent / "profile_sample.json"


def print_profile(data):
    """Общий вывод профиля для обоих источников. Отсутствующее значение (null) не выдумывается."""
    name = data.get("name")
    print(f"Логин: {data['login']}")
    print(f"ID: {data.get('id')}")
    print(f"Имя: {name if name is not None else 'не указано'}")


def load_sample():
    return read_json(SAMPLE_PATH)


def main():
    print("Источник профиля:")
    print("1. Сеть (GitHub API)")
    print("2. Локальный пример (profile_sample.json)")
    choice = input("Выбор: ").strip()
    try:
        if choice == "1":
            print_profile(fetch_profile(input("Логин GitHub: ")))
        elif choice == "2":
            print_profile(load_sample())
        else:
            print("Неизвестный пункт меню")
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
