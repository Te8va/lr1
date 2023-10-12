import numpy as np
import matplotlib.pyplot as plt

file_path = r"D:/ии/lr1/iris.txt"

data = np.loadtxt(file_path, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4), dtype={'names': ('X1', 'X2', 'X3', 'X4', 'Class'), 'formats': ('f8', 'f8', 'f8', 'f8', 'U15')})

class_setosa = data[data['Class'] == 'Iris-setosa']
class_versicolor = data[data['Class'] == 'Iris-versicolor']
class_virginica = data[data['Class'] == 'Iris-virginica']

fig, axes = plt.subplots(2,2, figsize=(9, 7))

axes[0, 0].scatter(class_setosa['X1'], class_setosa['X2'], label='Setosa', marker='o', color='r')
axes[0, 0].scatter(class_versicolor['X1'], class_versicolor['X2'], label='Versicolor', marker='s', color='g')
axes[0, 0].scatter(class_virginica['X1'], class_virginica['X2'], label='Virginica', marker='^', color='b')
axes[0, 0].set_xlabel('X1')
axes[0, 0].set_ylabel('X2')
axes[0, 0].legend()

axes[0, 1].scatter(class_setosa['X3'], class_setosa['X4'], label='Setosa', marker='o', color='r')
axes[0, 1].scatter(class_versicolor['X3'], class_versicolor['X4'], label='Versicolor', marker='s', color='g')
axes[0, 1].scatter(class_virginica['X3'], class_virginica['X4'], label='Virginica', marker='^', color='b')
axes[0, 1].set_xlabel('X3')
axes[0, 1].set_ylabel('X4')
axes[0, 1].legend()

axes[1, 0].scatter(class_setosa['X1'], class_setosa['X3'], label='Setosa', marker='o', color='r')
axes[1, 0].scatter(class_versicolor['X1'], class_versicolor['X3'], label='Versicolor', marker='s', color='g')
axes[1, 0].scatter(class_virginica['X1'], class_virginica['X3'], label='Virginica', marker='^', color='b')
axes[1, 0].set_xlabel('X1')
axes[1, 0].set_ylabel('X3')
axes[1, 0].legend()

axes[1, 1].scatter(class_setosa['X2'], class_setosa['X4'], label='Setosa', marker='o', color='r')
axes[1, 1].scatter(class_versicolor['X2'], class_versicolor['X4'], label='Versicolor', marker='s', color='g')
axes[1, 1].scatter(class_virginica['X2'], class_virginica['X4'], label='Virginica', marker='^', color='b')
axes[1, 1].set_xlabel('X2')
axes[1, 1].set_ylabel('X4')
axes[1, 1].legend()

plt.tight_layout()
plt.show()
