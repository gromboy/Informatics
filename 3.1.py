def circumference_length(radius):
    pi = 3.14159  # Значение числа Пи
    length = 2 * pi * radius  # Формула для длины окружности: 2 * pi * r
    return length

radius = float(input("Введите радиус окружности: "))
print("Длина окружности с радиусом", radius, ":", circumference_length(radius))
