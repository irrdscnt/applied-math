from sympy import symbols, simplify

def lagrange_interpolation(x_values, y_values):
    x = symbols('x')
    n = len(x_values)
    
    # Вычисление полинома Лагранжа
    lagrange_poly = 0
    for i in range(n):
        term = 1
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        lagrange_poly += y_values[i] * term
    
    return simplify(lagrange_poly)


def newton_interpolation(x_values, y_values):
    x = symbols('x')
    n = len(x_values)
    
    # Вычисление разделенных разностей
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x_values[i + j] - x_values[i])

    # Вычисление полинома Ньютона
    newton_poly = f[0][0]
    term = 1
    for i in range(1, n):
        term *= (x - x_values[i - 1])
        newton_poly += f[0][i] * term

    return simplify(newton_poly)

# Заданные точки
x_values = [0, 2, 3]
y_values = [2, 0, 4]

# Интерполяционные полиномы
lagrange_poly = lagrange_interpolation(x_values, y_values)
newton_poly = newton_interpolation(x_values, y_values)

print("Полином Лагранжа:")
print(lagrange_poly)

print("\nПолином Ньютона:")
print(newton_poly)
