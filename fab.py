# Определяем функцию, которую мы хотим интегрировать
def f(x):
    return x**3 + 2

# Начальная и конечная точки интервала
a = -1
b = 3

# Количество интервалов
n = 8

# Метод трапеций
def trapezoidal_method():
    delta_x = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    print(f"Iteration 0: Interval = [{a}, {b}], Integral = {integral:.4f}")
    for i in range(1, n):  # Изменено начальное значение i
        x_i = a + i * delta_x
        interval_start = a + (i - 1) * delta_x  # Изменено начальное значение интервала
        interval_end = x_i
        integral += f(x_i)
        print(f"Iteration {i}: Interval = [{interval_start}, {interval_end}], Integral = {integral:.4f}")
    integral *= delta_x
    return integral

# Исправленный код с учетом правильных значений f(a) и f(b)
f_a = f(a)
f_b = f(b)
integral_trapezoidal = trapezoidal_method()
print(f"f(a) = {f_a:.4f}, f(b) = {f_b:.4f}")
print(f"Интеграл методом трапеций: {integral_trapezoidal:.4f}")
