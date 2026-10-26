"""Дополнительно: окно поиска и просмотра записей (tkinter). Логика поиска — find_records()."""
import tkinter as tk
from tkinter import messagebox, ttk

from task_12.logic import find_records, sorted_by_id
from task_12.main import DEFAULT_PATH, format_record
from task_12.storage import load_records


def records_to_show(records, query):
    """Пустой запрос — все записи по id, иначе результат find_records()."""
    if query.strip() == "":
        return sorted_by_id(records)
    return find_records(records, query)


def build_window(root, records):
    root.title("План тренировок")
    query = tk.StringVar()
    status = tk.StringVar(value="Введите часть названия или оставьте поле пустым")

    entry = ttk.Entry(root, textvariable=query, width=40)
    entry.pack(padx=12, pady=(12, 4))
    listbox = tk.Listbox(root, width=70, height=12)
    listbox.pack(padx=12, pady=4)
    ttk.Label(root, textvariable=status).pack(padx=12, pady=(4, 12))

    def search():
        found = records_to_show(records, query.get())
        listbox.delete(0, tk.END)
        for record in found:
            listbox.insert(tk.END, format_record(record))
        status.set(f"Найдено записей: {len(found)}" if found else "Ничего не найдено")

    ttk.Button(root, text="Найти", command=search).pack(pady=4)
    entry.bind("<Return>", lambda event: search())
    search()
    return query, listbox, status


def main():
    try:
        records = load_records(DEFAULT_PATH)
    except (OSError, ValueError) as error:
        messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {error}")
        return
    root = tk.Tk()
    build_window(root, records)
    root.mainloop()


if __name__ == "__main__":
    main()
