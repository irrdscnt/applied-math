import numpy as np

# Исходные данные

supplies = np.array([250, 320, 150])
demands = np.array([210, 190, 260, 60])
costs = np.array([
    [7, 8, 1, 2],
    [3, 4, 5, 7],
    [9, 9, 8, 6]
])

# Создаем пустую матрицу для опорного плана
optimal_solution = np.zeros(costs.shape)

# Индексы текущего склада и потребителя
current_supplier = 0
current_consumer = 0

# Пока не достигнуты все потребности
while current_consumer < len(demands):
    # Находим минимум из доступных запасов и потребностей
    min_supply = supplies[current_supplier]
    min_demand = demands[current_consumer]
    min_value = min(min_supply, min_demand)

    # Заполняем опорную ячейку согласно методу северо-западного угла
    optimal_solution[current_supplier, current_consumer] = min_value

    # Уменьшаем соответствующие запасы и потребности
    supplies[current_supplier] -= min_value
    demands[current_consumer] -= min_value

    # Если запас на текущем складе исчерпан, переходим к следующему складу
    if supplies[current_supplier] == 0:
        current_supplier += 1

    # Если потребность удовлетворена, переходим к следующему потребителю
    if demands[current_consumer] == 0:
        current_consumer += 1

costs_for_shipments = optimal_solution * costs

total_cost = np.sum(costs_for_shipments)

print("Значение целевой функции (метод северо-западного угла):", total_cost)
print("Опорный план методом северо-западного угла:")
print(optimal_solution)

import numpy as np

# Исходные данные

supplies = np.array([250, 320, 150])
demands = np.array([210, 190, 260, 60])
costs = np.array([
    [7, 8, 1, 2],
    [3, 4, 5, 7],
    [9, 9, 8, 6]
])

#Создаем пустую матрицу для опорного плана
optimal_solution = np.zeros(costs.shape)

# Создаем список пар (стоимость, индексы) для ячеек с наименьшими стоимостями
cost_index_pairs = []

# Поиск ячеек с наименьшей стоимостью и добавление их в список
for i in range(costs.shape[0]):
    for j in range(costs.shape[1]):
        cost_index_pairs.append((costs[i, j], i, j))

# Сортировка списка по стоимости (в порядке возрастания)
cost_index_pairs.sort()

# Индексы текущего склада и потребителя
current_supplier = 0
current_consumer = 0

# Заполнение опорного плана согласно методу наименьшей стоимости
for cost, i, j in cost_index_pairs:
    supply = supplies[i]
    demand = demands[j]
    quantity = min(supply, demand)

    optimal_solution[i, j] = quantity

    supplies[i] -= quantity
    demands[j] -= quantity

costs_for_shipments = optimal_solution * costs

total_cost = np.sum(costs_for_shipments)

# Выводим итоговую цену (значение целевой функции)
print("Значение целевой функции (минимальная стоимость):", total_cost)

# Вывод опорного плана
print("Опорный план методом наименьшей стоимости:")
print(optimal_solution)
