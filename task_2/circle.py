# Дополнительно: длина окружности и площадь круга по положительному радиусу.
import math

radius = float(input("Радиус (> 0): "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь круга: {area:.2f}")
