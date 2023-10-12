import numpy as np

v1 = np.random.randint(-10, 10, 3)
v2 = np.random.randint(-10, 10, 3)

d = np.sqrt(np.sum((v1 - v2) ** 2))

print("Вектор v1:", v1)
print("Вектор v2:", v2)
print("Евклидово расстояние d:", d)
