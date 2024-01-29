import math

def F(x):
    return x + math.log(x / 3)

def check_initial_values(a, b):
    if F(a) * F(b) > 0:
        print("Ошибка: F(a) и F(b) должны иметь разные знаки для корректной работы метода хорд.Введите другие значения a,b")
        return False
    return True

def program_chord():
    a = 2
    b = 1
    eps = 0.01

    if not check_initial_values(a, b):
        return

    iteration = 1
    
    while True:
        fa = F(a)
        fb = F(b)
        x = a - (fa * (b - a)) / (fb - fa)
        print(f"Итерация {iteration}: x = {x}")
        
        if abs(x - a) < eps:
            break
        
        a = x
        iteration += 1

    print(f"Найденный корень: {x}")
    print(f"Значение функции в корне: {F(x)}")

program_chord()

# import math
# import matplotlib.pyplot as plt
# import numpy as np

# def F(x):
#     return x + math.log(x / 3)

# def program_chord():
#     a = float(input("Введите начальное значение a: "))
#     b = float(input("Введите начальное значение b: "))
#     eps = float(input("Введите желаемую точность (eps): "))
    
#     iteration = 1
#     x_values = []
    
#     while True:
#         fa = F(a)
#         fb = F(b)
#         x = a - (fa * (b - a)) / (fb - fa)
#         x_values.append(x)
        
#         print(f"Итерация {iteration}: x = {x}")
        
#         if abs(x - a) < eps:
#             break
        
#         a = x  
#         iteration += 1

#     print(f"Найденный корень: {x}")
#     print(f"Значение функции в корне: {F(x)}") 
    
#     # Построение графика функции и отметка точек
#     x_range = np.linspace(0.1, 2.0, 400)
#     y_range = [F(x) for x in x_range]
#     plt.plot(x_range, y_range, label='F(x)')
#     plt.scatter(x_values, [F(x) for x in x_values], c='red', marker='o', label='Итерационные точки')
#     plt.xlabel('x')
#     plt.ylabel('F(x)')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# program_chord()