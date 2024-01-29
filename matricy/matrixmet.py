import numpy as np

# Задаем матрицы A и B
A = np.array([[2, -5, 3],
              [3, -4, 2],
              [1, 4, -5]])

B = np.array([[-25, -11, -17],
              [-26, -6, -19],
              [7, 14, -2]])

# Решаем матричное уравнение AX = B
A_inverted=np.linalg.inv(A)
X = np.linalg.solve(A, B)
print(f"Обратная матрица А:",A_inverted)
print("Решение X:")
print(X)

# # Задаем матрицы A и B, удостоверьтесь, что они имеют тип данных float64
# A = np.array([[2.0, -5.0, 3.0],
#               [3.0, -4.0, 2.0],
#               [1.0, 4.0, -5.0]])

# B = np.array([[-25.0, -11.0, -17.0],
#               [-26.0, -6.0, -19.0],
#               [7.0, 14.0, -2.0]])

# # Размерность матрицы A
# n = len(A)

# # Создаем расширенную матрицу [A|B]
# augmented_matrix = np.hstack((A, B))

# # Прямой ход (forward elimination)
# for i in range(n):
#     pivot_row = i
#     for j in range(i + 1, n):
#         if abs(augmented_matrix[j, i]) > abs(augmented_matrix[pivot_row, i]):
#             pivot_row = j

#     # Поменять строки, если необходимо
#     if pivot_row != i:
#         augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

#     pivot = augmented_matrix[i, i]
#     if pivot == 0:
#         raise ValueError("Матрица коэффициентов вырожденная, метод Гаусса не применим")

#     augmented_matrix[i, :] /= pivot

#     for j in range(i + 1, n):
#         factor = augmented_matrix[j, i]
#         augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

# # Обратный ход (backward substitution)
# X = np.zeros((n, n))
# for i in range(n - 1, -1, -1):
#     X[i, :] = augmented_matrix[i, -n:]
#     for j in range(i + 1, n):
#         X[i, :] -= augmented_matrix[i, j] * X[j, :]

# print("Решение X:")
# print(X)
