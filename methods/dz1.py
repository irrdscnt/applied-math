import math

def equation(x):
    return x + math.log(x / 3)
    # return x**3+x-1


# Начальные значения интервала
a = 1.0
b = 2.5
tolerance = 0.01
iteration = 0

while (b - a)  > tolerance:
    c = (a + b) / 2
    print(f"Итерация {iteration}: Интервал: [{a}, {b}],b-a :{b-a}, Корень: {c}")
    if equation(c) == 0:
        break
    elif equation(a) * equation(c) < 0:
        b = c
    else:
        a = c
    iteration+=1


solution = (a + b) / 2

print(f"Итоговое решение: x = {solution},Значение функции в корне: {equation(solution)},Количество итераций: {iteration}, b-a :{b-a}")

# import math

# def equation(x):
#     return x + math.log(x/3)

# def derivative(x):
#     return 1 + 1/x

# def newton_method(equation, derivative, initial_guess, tolerance, max_iterations):
#     x = initial_guess
#     iteration = 0

#     while abs(equation(x)) > tolerance and iteration < max_iterations:
#         x = x - equation(x) / derivative(x)
#         iteration += 1

#     if abs(equation(x)) <= tolerance:
#         return x
#     else:
#         return None

# initial_guess = 1.0
# tolerance = 0.001
# max_iterations = 30


# solution = newton_method(equation, derivative, initial_guess, tolerance, max_iterations)

# if solution is not None:
#     print(f"Решение уравнения: x + ln(x/3) = 0 с точностью {tolerance} равно x = {solution}")
# else:
#     print("Метод Ньютона не сходится на данном отрезке.")
print("Метод Ньютона ")
import math

def equation(x):
    return x + math.log(x/3)

def derivative(x):
    return 1 + 1/x

def newton_method(equation, derivative, initial_guess, tolerance, max_iterations):
    x = initial_guess
    iteration = 0

    while abs(equation(x)) > tolerance and iteration < max_iterations:
        x_old = x
        x = x - equation(x) / derivative(x)
        iteration += 1
        print(f'Итерация {iteration}: x = {x}, Значение функции = {equation(x)}')

    if abs(equation(x)) <= tolerance:
        return x
    else:
        return None

initial_guess = 1
tolerance = 0.01
max_iterations = 30

solution = newton_method(equation, derivative, initial_guess, tolerance, max_iterations)

if solution is not None:
    print(f"Решение уравнения: x + ln(x/3) = 0 с точностью {tolerance} равно x = {solution},Значение функции = {equation(solution)}")
else:
    print("Метод Ньютона не сходится на данном отрезке.")

