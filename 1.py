import numpy as np

A = np.random.randint(-10, 10, 10)

B = A[A < 0]

sumB = np.sum(B)

print("Вектор A:", A)
print("Вектор B:", B)
print("Сумма отрицательных элементов:", sumB)