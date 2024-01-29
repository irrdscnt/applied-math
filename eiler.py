def f(x, y):
    return y + 5 * x - 1

def euler_method(x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < x_end:
        x_i = x_values[-1]
        y_i = y_values[-1]
        y_next = y_i + h * f(x_i, y_i)

        x_values.append(x_i + h)
        y_values.append(y_next)

    return x_values, y_values

def modified_euler_method(x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < x_end:
        x_i = x_values[-1]
        y_i = y_values[-1]
        k1 = h * f(x_i, y_i)
        k2 = h * f(x_i + h, y_i + k1)
        y_next = y_i + (k1 + k2) / 2

        x_values.append(x_i + h)
        y_values.append(y_next)

    return x_values, y_values

def runge_kutta_method(x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < x_end:
        x_i = x_values[-1]
        y_i = y_values[-1]
        k1 = h * f(x_i, y_i)
        k2 = h * f(x_i + h/2, y_i + k1/2)
        k3 = h * f(x_i + h/2, y_i + k2/2)
        k4 = h * f(x_i + h, y_i + k3)
        y_next = y_i + (k1 + 2*k2 + 2*k3 + k4) / 6

        x_values.append(x_i + h)
        y_values.append(y_next)

    return x_values, y_values

# Заданные параметры
x0 = 0
y0 = 2
h = 0.8
x_end = 3.2

# Решение методом Эйлера
x_euler, y_euler = euler_method(x0, y0, h, x_end)

# Решение модифицированным методом Эйлера
x_modified_euler, y_modified_euler = modified_euler_method(x0, y0, h, x_end)

# Решение методом Рунге-Кутта
x_runge_kutta, y_runge_kutta = runge_kutta_method(x0, y0, h, x_end)
print(f"Eiler method : {x_euler, y_euler}")
print(f"Modified Eiler Method : {x_modified_euler, y_modified_euler}")
print(f"Runge-Kutta method : {x_runge_kutta, y_runge_kutta}")
