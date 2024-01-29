import numpy as np
import matplotlib.pyplot as plt

# Задаем данные (пример)
x = np.array([2.6, 2.8, 2.9, 3.4 ,4.6 ,5.2 ,6.1 ,7.7 ,10.6 ,14 ])
y = np.array([19, 18, 20, 23, 26, 31, 37, 45, 53, 68])

# Вычисляем средние значения x и y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Вычисляем параметры линейной регрессии (наклон и пересечение)
slope = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x)**2)
intercept = mean_y - slope * mean_x

# Выводим уравнение линейной регрессии
print(f"Уравнение линейной регрессии: y = {slope:.2f}x + {intercept:.2f}")

# Строим график
plt.scatter(x, y, label='Исходные данные')
plt.plot(x, slope * x + intercept, color='red', label='Линейная регрессия')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
