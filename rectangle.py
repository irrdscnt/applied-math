# Определяем функцию, которую мы хотим интегрировать
def f(x):
    return x**3 + 2

# Начальная и конечная точки интервала
a = -1
b = 3

# Количество интервалов
n = 8

# Шаг интегрирования
delta_x = (b - a) / n

# Метод левых прямоугольников
def left_rectangle_method():
    print(f"Метод левых прямоугольников")
    integral = 0
    for i in range(n):
        x_i = a + i * delta_x
        integral += f(x_i)
        print(f"Iteration {i}: Interval = [{x_i}, {x_i + delta_x}], Integral = {integral:.4f}")
    integral *= delta_x
    return integral

# Метод правых прямоугольников
def right_rectangle_method():
    print(f"Метод правых прямоугольников")
    integral = 0
    for i in range(1, n + 1):
        x_i = a + i * delta_x
        integral += f(x_i)

        print(f"Iteration {i}: Interval = [{x_i - delta_x}, {x_i}], Integral = {integral:.4f}")
    integral *= delta_x
    return integral

# Метод средних прямоугольников
def middle_rectangle_method():
    print(f"Метод средних прямоугольников")
    integral = 0
    for i in range(n):
        x_i = a + (i + 0.5) * delta_x
        integral += f(x_i)
        print(f"Iteration {i}: Interval = [{x_i - 0.5 * delta_x}, {x_i + 0.5 * delta_x}], Integral = {integral:.4f}")
    integral *= delta_x
    return integral

integral_left_rectangle = left_rectangle_method()
integral_right_rectangle = right_rectangle_method()
integral_middle_rectangle = middle_rectangle_method()
ActValue = 28
print(f'Точное значение интеграла {ActValue}')
print(f"Формула левых прямоугольников")
print(f"Интеграл методом левых прямоугольников: {integral_left_rectangle:.4f}")
print(f'Абсолютная Погрешность {abs(ActValue - integral_left_rectangle)}')
print(f'Относительная погрешность {abs(ActValue - integral_left_rectangle) / abs(ActValue):.5f}')

print(f"Формула правых прямоугольников")
print(f"Интеграл методом правых прямоугольников: {integral_right_rectangle:.4f}")
print(f'Абсолютная Погрешность {abs(ActValue - integral_right_rectangle)}')
print(f'Относительная погрешность {abs(ActValue - integral_right_rectangle) / abs(ActValue):.5f}')

print(f"Формула средних прямоугольников")
print(f"Интеграл методом средних прямоугольников: {integral_middle_rectangle:.4f}")
print(f'Абсолютная Погрешность {abs(ActValue - integral_middle_rectangle)}')
print(f'Относительная погрешность {abs(ActValue - integral_middle_rectangle) / abs(ActValue):.5f}')
