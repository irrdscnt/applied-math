import pulp

# Создаем задачу для максимизации прибыли
problem = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Определяем переменные решения
x = pulp.LpVariable("Valves", lowBound=0, upBound=250, cat="Integer")
y = pulp.LpVariable("Bushings", lowBound=0, upBound=340, cat="Integer")

# Определяем целевую функцию для максимизации прибыли
profit = 800 * x + 720 * y
problem += profit

# Определяем ограничения
work_hours_constraint = 3 * x + 2.4 * y <= 900
problem += work_hours_constraint

# Решаем задачу
problem.solve()

# Выводим результаты
if problem.status == pulp.LpStatusOptimal:
    optimal_profit = pulp.value(problem.objective)
    optimal_valves = x.varValue
    optimal_bushings = y.varValue
    print("Максимальная прибыль:", optimal_profit)
    print("Оптимальное количество валов:", optimal_valves)
    print("Оптимальное количество втулок:", optimal_bushings)
else:
    print("Решение не найдено")

