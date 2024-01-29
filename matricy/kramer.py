import numpy as np

def kramer_solver(A, b):
    n = len(b)
    det_A = np.linalg.det(A)
    
    if det_A == 0:
        return "Матрица вырожденная,мтеод Крамера неприменим"
    
    x = np.zeros(n)
    
    for i in range(n):
        A_temp = A.copy()
        A_temp[:, i] = b
        det_A_temp = np.linalg.det(A_temp)
        x[i] = det_A_temp / det_A
    print("Determinant:",det_A)
    
    return x

A = np.array([[3, -5, -7],
              [2, 7, 7],
              [1, -4, -6]])

b = np.array([-7, 11, -10])

solution = kramer_solver(A, b)
print("Solution: ", solution)
