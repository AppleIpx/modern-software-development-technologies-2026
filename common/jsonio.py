import json


def read_json(path):
    """Прочитать JSON из файла в UTF-8. Ошибки (OSError, UnicodeError, JSONDecodeError) — вызывающему."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path, data):
    """Записать JSON в UTF-8: читаемая кириллица, отступ 2."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
