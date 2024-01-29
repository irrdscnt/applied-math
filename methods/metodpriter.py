# import math 

# def F(x):
#     # return x**3 + x - 1
#     return x + math.log(x / 3)


# def program3():
#     x = float(input("Введите начальное значение x: "))
#     eps = float(input("Введите желаемую точность (eps): "))
#     M = float(input("Введите значение M: "))

#     while True:
#         xk = x - F(x) / M
#         if abs(xk - x) < eps:
#             break
#         x = xk

#     print(f"Найденный корень: {xk}")
#     print(f"Значение функции в корне: {F(xk)}")

# program3()

import math

def F(x):
    return x + math.log(x / 3)

def find_M():
    b = 1
    max_derivative = max(1 + 1 / x for x in [b])
    return max_derivative

def simple_iteration():
    x = 0.5
    eps = 0.01
    M = find_M()
    print(f"Найденное значение М= {M}")
    iteration = 1
    
    while True:
        xk = x - F(x) / M
        print(f"Итерация {iteration}: x = {xk}")
        if abs(xk - x) < eps:
            break
        x = xk
        iteration += 1

    print(f"Найденный корень: {xk}")
    print(f"Значение функции в корне: {F(xk)}")

simple_iteration()
