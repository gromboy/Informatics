def circle_area(radius):
    pi = 3.14159  # Значение числа Пи
    area = pi * radius ** 2  # Формула для площади круга: pi * r^2
    return area

radius = float(input("Введите радиус круга: "))
print("Площадь круга с радиусом", radius, ":", circle_area(radius))
