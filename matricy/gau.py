import numpy as np

# Заданные матрицы A и b
A = np.array([[2.0, 1.0, -1.0],
              [3.0, -4.0, 5.0],
              [5.0, 3.0, 4.0]], dtype=float)

b = np.array([0.0, -11.0, -11.0], dtype=float)

# Размерность матрицы A
n = A.shape[0]

# Создаем расширенную матрицу (A|b)
augmented_matrix = np.column_stack((A, b))

# Прямой ход метода Гаусса
for i in range(n):
    # Поиск максимального элемента в текущем столбце для выбора ведущей строки
    max_row = i
    for j in range(i + 1, n):
        if abs(augmented_matrix[j, i]) > abs(augmented_matrix[max_row, i]):
            max_row = j

    # Обмен строками
    augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

    # Приведение текущего столбца к единичному элементу
    pivot = augmented_matrix[i, i]
    augmented_matrix[i] /= pivot

    # Вычитание текущей строки из остальных строк для обнуления столбца
    for j in range(i + 1, n):
        factor = augmented_matrix[j, i]
        augmented_matrix[j] -= factor * augmented_matrix[i]

# Обратный ход метода Гаусса
x = np.zeros(n, dtype=float)
for i in range(n - 1, -1, -1):
    x[i] = augmented_matrix[i, -1]
    for j in range(i + 1, n):
        x[i] -= augmented_matrix[i, j] * x[j]

print("Решение системы уравнений:")
print(x)
