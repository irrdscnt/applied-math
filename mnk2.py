import numpy as np

x = np.array([2.6, 2.8, 2.9, 3.4, 4.6, 5.2, 6.1, 7.7, 10.6, 14])
y = np.array([19, 18, 20, 23, 26, 31, 37, 45, 53, 68])

n = len(x)
sum_x = np.sum(x)
# print(sum_x)
sum_y = np.sum(y)
# print(sum_y)
sum_xy = np.sum(x * y)
# print(sum_xy)
sum_x_squared = np.sum(x**2)

# Вычисление коэффициентов линейной регрессии
k = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
b = (sum_y - k * sum_x) / n

# Вывод коэффициентов
print("k =", k)
print("b =", b)

# Прогнозирование значения y при x = 2 млн. руб.
x_pred = 2
y_pred = k * x_pred + b

print("Прогноз среднесуточной производительности при стоимости основных производственных фондов 2 млн. руб.:", y_pred)
