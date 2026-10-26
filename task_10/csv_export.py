# Дополнительно: экспорт matrix.txt в matrix.csv стандартным модулем csv.
from pathlib import Path

from task_10.files_lab import export_csv, read_matrix

folder = Path(__file__).resolve().parent
matrix = read_matrix(folder / "matrix.txt")
export_csv(matrix, folder / "matrix.csv")
print(f"Записано строк: {len(matrix)} → matrix.csv")
