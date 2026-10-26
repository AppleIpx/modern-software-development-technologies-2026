"""Чтение и запись JSON без консольных диалогов."""
import json
import os
from pathlib import Path

from task_12.logic import validate_records


def load_records(path):
    """Прочитать и проверить файл. Исключения (FileNotFoundError, UnicodeError, JSONDecodeError,
    ValueError, OSError) передаются вызывающему коду. Файл не изменяется."""
    with open(path, "r", encoding="utf-8") as file:
        records = json.load(file)
    validate_records(records)
    return records


def save_records(path, records):
    """Записать записи в JSON (UTF-8). Сначала пишется временный файл, затем он заменяет целевой,
    поэтому при ошибке прежний файл остаётся целым. Ошибки записи — исключением."""
    validate_records(records)
    path = Path(path)
    temp_path = path.with_name(path.name + ".tmp")
    try:
        with open(temp_path, "w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
        os.replace(temp_path, path)
    except OSError:
        try:
            temp_path.unlink()
        except OSError:
            pass
        raise
