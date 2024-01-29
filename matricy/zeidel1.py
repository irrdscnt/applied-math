import numpy as np

# Матрица коэффициентов A
A = np.array([[-3.0, 1.2, 0.0, 0.0, 0.0],
              [2.0, -5.0, 1.0, 0.0, 0.0],
              [0.0, 1.1, 4.0, -1.0, 0.0],
              [0.0, 0.0, 5.0, 9.0, 2.0],
              [0.0, 0.0, 0.0, -2.0, 6.5]])

# Вектор правой части b
b = np.array([-1.7, -2.0, 3.0, 11.0, 2.0])

# Начальное приближение для x (все значения равны 0)
x = np.zeros_like(b)

# Максимальное количество итераций
max_iterations = 1000

# Точность
tolerance = 0.01

for i in range(max_iterations):
    x_new = np.copy(x)
    for j in range(len(b)):
        x_new[j] = (b[j] - np.dot(A[j, :j], x_new[:j]) - np.dot(A[j, j+1:], x[j+1:])) / A[j, j]
    if np.all(np.abs(x_new - x) < tolerance):
        break
    x = x_new

print("Решение методом Зейделя:", x)
