# Определяем функцию, которую мы хотим интегрировать
def f(x):
    return pow(x, 3) + 2


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
    for i in range(1,n):
        x_i = a + i * delta_x
        interval_start = a + (i - 1) * delta_x  
        interval_end = x_i
        integral += f(x_i)
        print(f"Iteration {i}: Interval = [{interval_start}, {interval_end}], Integral = {integral:.4f}")
    integral *= delta_x
    return integral

integral_trapezoidal = trapezoidal_method()
print(f"Интеграл методом трапеций: {integral_trapezoidal:.1f}")

