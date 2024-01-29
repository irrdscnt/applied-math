# def f(x):
#     return x**3 + 2

# def rectangular_integration(a, b, n):
#     delta_x = (b - a) / n
#     integral = 0.0
    
#     for i in range(n):
#         x_i = a + i * delta_x + delta_x / 2  # Выбираем среднюю точку подинтервала
#         f_i = f(x_i)
#         integral += f_i * delta_x

#     return integral

# a = -1
# b = 3
# n = 8

# result = rectangular_integration(a, b, n)

# print("Результат интегрирования методом прямоугольников:", result)

def f(x):
    return x**3 + 2

def rectangular_integration(a, b, n):
    delta_x = (b - a) / n
    integral = 0.0
    for i in range(n):
        x_i = a + i * delta_x
        integral += f(x_i) * delta_x

    return integral

a = -1
b = 3
n = 8

result = rectangular_integration(a, b, n)
ActValue = 28
print(f'Абсолютная Погрешность {abs(ActValue - result)}')
print(f'Относительная погрешность {abs(ActValue - result) / abs(ActValue)}')
print("Результат интегрирования методом прямоугольников:", result)
