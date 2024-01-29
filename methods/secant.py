import math

def F(x):
    return x + math.log(x / 3)

def secant_method(x1, x2, epsilon):

    iteration = 1
    
    while True:
        fx1 = F(x1)
        fx2 = F(x2)
        x3 = x2 - (fx2 * (x2 - x1)) / (fx2 - fx1)
        
        print(f"Итерация {iteration}: x = {x3}")
        
        if F(x3)<= eps:
            break
        x2 = x3
        iteration += 1
    
    print(f"Найденный корень: {x3}")
    print(f"Значение функции в корне: {F(x3)}")


eps = 0.01
x1=1
x2=2

secant_method(x1, x2, eps)