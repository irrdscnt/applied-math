#метод хорд
import math


def f(x):
    return x + math.log(x/3)


def chord_method(a, b, epsilon):
    x0 = a
    iterations = 0    
    while True:
        iterations += 1        
        x1 = x0 - (f(x0) * (b - x0)) / (f(b) - f(x0))


        error = abs(x1 - x0)


        print(f"Iteration {iterations}: x = {x1}, погрешность = {error}, f(x) = {f(x1)}, f0 = {f(x0)},fb =  {f(b)} ")

        if error < epsilon:
            break        
        x0 = x1

    return x1


a = 1
b = 2

epsilon = 0.01
result = chord_method(a, b, epsilon)

print(f"\nРезультат: x = {result},{f(result)}")