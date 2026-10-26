# Режим без сети: учебные локальные данные из profile_sample.json.
from pathlib import Path

from common.jsonio import read_json

data = read_json(Path(__file__).resolve().parent / "profile_sample.json")

print(f"Логин: {data['login']} (использованы учебные локальные данные)")
