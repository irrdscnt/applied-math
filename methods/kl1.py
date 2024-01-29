def simple_iteration_method(g, x0, epsilon, max_iterations):
    x = x0
    iterations = 0

    while iterations < max_iterations:
        x_next = g(x)
        print(f"Iteration {iterations + 1}: x = {x_next:.10f}")
        if abs(x_next - x) < epsilon:
            return x_next
        x = x_next
        iterations += 1

    raise Exception("Не удалось найти корень с заданной точностью.")

# Функция g(x) для уравнения x^3 + x - 1 = 0
def g(x):
    return x**3 + x - 1

# Начальное приближение и другие параметры
x0 = 1.0  # Начальное приближение
epsilon = 0.01  # Точность с большим количеством знаков
max_iterations = 100  # Максимальное количество итераций

# Вызываем метод простой итерации
result = simple_iteration_method(g, x0, epsilon, max_iterations)
print(f"Приближенный корень: {result:.10f}")
