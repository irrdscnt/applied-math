# import math

# def F(x):
#     return x + math.log(x / 3)

# def check_initial_values(a, b):
#     if F(a) * F(b) > 0:
#         print("Ошибка: F(a) и F(b) должны иметь разные знаки для корректной работы метода хорд.Введите другие значения a,b")
#         return False
#     return True

# def program_chord():
#     x2 = 2
#     x1 = 1
#     eps = 0.01

#     if not check_initial_values(a, b):
#         return

#     iteration = 1
    
#     while True:
#         fx2 = F(x2)
#         fx1 = F(x1)
#         fxx = ((fx2-fx1)/(x2-x1))*((xx-x1)+fx1)
#         print(f"Итерация {iteration}: x = {x}")
        
#         if abs(x - a) < eps:
#             break
        
#         a = x
#         iteration += 1

#     print(f"Найденный корень: {x}")
#     print(f"Значение функции в корне: {F(x)}")

# program_chord()

import math

def equation(x):
    return x + math.log(x/3)

def chord_method(a, b, tolerance):
    iteration = 0

    while abs(b - a) > tolerance:
        x = a - (equation(a) * (b - a)) / (equation(b) - equation(a))
        a, b = b, x
        iteration += 1

    return (a + b) / 2

a = 2.0  # Начальное значение a
b = 1.0 # Начальное значение b
tolerance = 0.01

root = chord_method(a, b, tolerance)

print(f"Решение уравнения x + ln(x/3) = 0 с точностью {tolerance} равно x = {root},{equation(root)}")
