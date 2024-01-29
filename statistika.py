import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Значения выборки
data = [0.938, 2.26, -0.147, 1.051, 2.046, -1.322, 1.808, -0.549, 0.959, -0.552, -0.742, 0.924, -1.417, 0.376, 0.913,
        1.966, -0.729, 0.115, 0.976, 0.686, 0.696, 1.021, 1.323, 1.431, 1.397, 0.76, -0.193, 0.966, 0.349, -0.363,
        2.614, -0.736, -1.194, 0.886, -0.929, 0.089, 1.374, -0.069, -0.41, -0.368, 1.597, -0.523, -0.752, 1.125,
        -0.238, 1.041, 1.164, 1.02, 0.646, 0.449]

# Построение гистограммы
plt.hist(data, bins=10, edgecolor='black', alpha=0.7)
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма выборки')
plt.show()

# Вычисление выборочного среднего
mean_value = np.mean(data)
print(f'Выборочное среднее: {mean_value}')

# Вычисление выборочной дисперсии (исправленной)
variance_value = np.var(data, ddof=1)
print(f'Выборочная дисперсия: {variance_value}')

# Вычисление выборочной медианы
median_value = np.median(data)
print(f'Выборочная медиана: {median_value}')

# Вычисление моды (если она существует)
mode_result = stats.mode(data)
if mode_result.count[0] > 1:
    print(f'Выборочная мода: {mode_result.mode[0]} (встречается {mode_result.count[0]} раз)')
else:
    print('Выборочная мода не определена (все значения уникальны)')
