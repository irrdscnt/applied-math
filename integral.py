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

def rectangle_method():
    integral = 0
    for i in range(n):
        x_i = a + i * delta_x
        integral += f(x_i) * delta_x
    return integral

# Метод трапеций
def trapezoidal_method():
    integral = 0.5 * (f(a) + f(b))
    for i in range(n):
        x_i = a + i * delta_x
        integral += f(x_i)
    integral *= delta_x
    return integral

# Метод Симпсона (парабол)
def simpson_method():
    integral = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * delta_x
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)
    integral *= delta_x / 3
    return integral

# Вычисляем интегралы
integral_trapezoidal = trapezoidal_method()
integral_simpson = simpson_method()
integral_rectangle=rectangle_method()
# Выводим результат
print(f"Интеграл методом трапеций: {integral_trapezoidal:.4f}")
print(f"Интеграл методом Симпсона: {integral_simpson:.4f}")
ActValue = 28
print(f'Абсолютная Погрешность {abs(ActValue - integral_simpson)}')
print(f'Относительная погрешность {abs(ActValue - integral_simpson) / abs(ActValue)}')

# print(f"Интеграл методом Прямоугольников: {integral_rectangle:.4f}")

