import numpy as np

def gaussian_elimination(A, b):
    n = len(b)

    # Прямой ход (forward elimination)
    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(A[j, i]) > abs(A[pivot_row, i]):
                pivot_row = j

        # Поменять строки, если необходимо
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
            b[i], b[pivot_row] = b[pivot_row], b[i]

        pivot = A[i, i]
        if pivot == 0:
            raise ValueError("Матрица коэффициентов вырожденная, метод Гаусса не применим")

        for j in range(i + 1, n):
            factor = A[j, i] / pivot
            b[j] -= factor * b[i]
            A[j, i:] -= factor * A[i, i:]

    # Обратный ход (backward substitution)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

# A = np.array([[2.0, 1.0, -1.0],
#               [3.0, -4.0, 5.0],
#               [5.0, 3.0, 4.0]], dtype=float)

# b = np.array([0.0, -11.0, -11.0], dtype=float)
    A = np.array([[3.0, -5.0, -7.0],
                [2.0, 7.0, 7.0],
                [1.0, -4.0, -6.0]])

    b = np.array([-7.0, 11.0, -10.0])
solution = gaussian_elimination(A, b)
print("Решение:", solution)