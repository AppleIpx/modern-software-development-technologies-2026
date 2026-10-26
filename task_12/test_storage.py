import json
from pathlib import Path
from tempfile import TemporaryDirectory

from task_12.storage import load_records, save_records

RECORDS = [
    {"id": 1, "title": "Утренняя пробежка", "category": "кардио", "amount": 30, "completed": True},
    {"id": 2, "title": "Растяжка", "category": "гибкость", "amount": 15, "completed": False},
]


def expect(exception_type, function, *args):
    try:
        function(*args)
    except exception_type:
        pass
    else:
        assert False, "Ошибка не обнаружена"


with TemporaryDirectory() as directory:
    folder = Path(directory)
    path = folder / "data.json"

    # Сохранение и повторная загрузка: все поля и статусы восстановлены
    save_records(path, RECORDS)
    assert load_records(path) == RECORDS
    assert "Утренняя пробежка" in path.read_text(encoding="utf-8")  # читаемая кириллица
    assert not (folder / "data.json.tmp").exists()

    # Пустой список
    save_records(path, [])
    assert load_records(path) == []

    # Отсутствующий файл
    expect(FileNotFoundError, load_records, folder / "нет.json")

    # Повреждённый JSON
    path.write_text("[{не json", encoding="utf-8")
    expect(json.JSONDecodeError, load_records, path)

    # Неправильная кодировка
    path.write_bytes(b"\xff\xfe\x00")
    expect(UnicodeError, load_records, path)

    # Неправильная структура и повторный id
    path.write_text('{"id": 1}', encoding="utf-8")
    expect(ValueError, load_records, path)
    duplicate = [dict(RECORDS[0]), dict(RECORDS[0])]
    path.write_text(json.dumps(duplicate, ensure_ascii=False), encoding="utf-8")
    expect(ValueError, load_records, path)

    # Загрузка не изменяет файл
    before = path.read_bytes()
    expect(ValueError, load_records, path)
    assert path.read_bytes() == before

    # Некорректные данные не записываются, прежний файл цел
    save_records(path, RECORDS)
    good = path.read_bytes()
    expect(ValueError, save_records, path, [{"id": 1}])
    assert path.read_bytes() == good

    # Ошибка записи (каталога нет): исключение, временных файлов нет
    expect(OSError, save_records, folder / "нет_каталога" / "data.json", RECORDS)

print("Все проверки пройдены")
