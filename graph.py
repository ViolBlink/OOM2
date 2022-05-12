import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

f = open('Config.txt')

Arr = f.read()
Arr = Arr.split("\n")

""" Считываем параметры """

T = []
names = []
figurs = []
axes = []

for i in range(8, len(Arr)):
    T.append(int(Arr[i]))
    names.append("data_" + Arr[i] + ".txt")
    figurs.append(plt.figure(figsize=(110, 110)))
    axes.append(figurs[i - 8].add_subplot(projection='3d'))
    axes[i - 8].set_title('Численное решение в момент времени t = ' + str(Arr[i]))
    axes[i - 8].set_ylabel('Координата y')
    axes[i - 8].set_xlabel('Координата x')
    axes[i - 8].set_zlabel('U(x,t)')

f.close()

f = open('x.txt')

X = []

for x in f:
    X.append(float(x))

f.close()

f = open('y.txt')

Y = []

for y in f:
    Y.append(float(y))

gx = np.ravel(X)
gy = np.ravel(Y)

f.close()

count = 0
for name in names:
    f = open(name)
    Arr = []
    # mas = f.read()
    # mas.split("\n")
    for x in f:
        Arr.append(float(x))   
    axes[count].plot_trisurf(X, Y, Arr, cmap=cm.jet, edgecolor='none')
    count += 1
    f.close()

plt.show()
