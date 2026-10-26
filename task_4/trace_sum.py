# Трассировка цикла суммирования чисел 1–4: значения переменных до и после каждой итерации.
total = 0
for number in range(1, 5):
    before = total
    total += number
    print(f"number={number}: total до={before}, после={total}")
