import numpy as np

# Матрица коэффициентов A
A = np.array([[-3.0, 1.2, 0.0, 0.0, 0.0],
              [2.0, -5.0, 1.0, 0.0, 0.0],
              [0.0, 1.1, 4.0, -1.0, 0.0],
              [0.0, 0.0, 5.0, 9.0, 2.0],
              [0.0, 0.0, 0.0, -2.0, 6.5]])

# Вектор правой части b
b = np.array([-1.7, -2.0, 3.0, 11.0, 2.0])

# Начальные приближения для x (можно выбрать любые начальные значения)
x0 = np.zeros_like(b)

# Максимальное количество итераций
max_iterations = 1000

# Параметр для остановки по требуемой точности
epsilon = 0.01

x = x0.copy()

for iteration in range(max_iterations):
    x_new = np.zeros_like(x)
    for i in range(len(b)):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]

    if np.allclose(x, x_new, epsilon):
        break

    x = x_new

print("Решение методом Якоби:", x)

# import numpy as np

# # Матрица коэффициентов A
# A = np.array([[-3.0, 1.2, 0.0, 0.0, 0.0],
#               [2.0, -5.0, 1.0, 0.0, 0.0],
#               [0.0, 1.1, 4.0, -1.0, 0.0],
#               [0.0, 0.0, 5.0, 9.0, 2.0],
#               [0.0, 0.0, 0.0, -2.0, 6.5]])

# # Вектор правой части b
# b = np.array([-1.7, -2.0, 3.0, 11.0, 2.0])

# # Начальное приближение
# x = np.zeros_like(b)

# # Максимальное количество итераций
# max_iterations = 1000

# # Точность
# tolerance = 1e-6

# for iteration in range(max_iterations):
#     for i in range(len(b)):
#         x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    
#     # Проверка на точность для завершения итераций
#     if np.all(np.abs(np.dot(A, x) - b) < tolerance):
#         break

# if iteration == max_iterations - 1:
#     print("Метод Гаусса-Зейделя не сошелся после", max_iterations, "итераций.")
# else:
#     print("Решение методом Гаусса-Зейделя:")
#     print("x =", x)
