# newton method
# from scipy.optimize import fsolve
# import numpy as np

# # Определение функции, представляющей систему уравнений
# def equations(vars):
#     x, y = vars
#     eq1 = np.sin(x + 1) - y - 1
#     eq2 = 2 * x + np.cos(y) - 2
#     return [eq1, eq2]

# # Начальное приближение
# initial_guess = [0.0, 0.0]

# # Решение системы уравнений
# solution = fsolve(equations, initial_guess)

# print("Решение методом Ньютона:")
# print("x =", solution[0])
# print("y =", solution[1])

# method simple iterations

import numpy as np

# Начальное приближение
x0 = 0.0
y0 = 0.0

# Максимальное количество итераций
max_iterations = 100

# Точность
tolerance = 1e-6

for iteration in range(max_iterations):
    # Вычисление новых значений x и y по методу простых итераций
    x_new = (2 - np.cos(y0)) / 2
    y_new = np.sin(x_new + 1) - 1
    
    # Проверка на точность для завершения итераций
    if abs(x_new - x0) < tolerance and abs(y_new - y0) < tolerance:
        break
    
    x0 = x_new
    y0 = y_new

if iteration == max_iterations - 1:
    print("Метод простых итераций не сошелся после", max_iterations, "итераций.")
else:
    print("Решение методом простых итераций:")
    print("x =", x_new)
    print("y =", y_new)
