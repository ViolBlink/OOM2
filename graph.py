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
axes1 = []
axes2 = []
axes3 = []

for i in range(8, len(Arr)):
    T.append(float(Arr[i]))
    names.append("data\\data_" + Arr[i])
    figurs.append(plt.figure(figsize=(15, 15)))
    axes1.append(figurs[i - 8].add_subplot(1, 3, 1, projection='3d'))
    axes1[i - 8].set_title('Численное решение в момент\n времени t = ' + str(Arr[i]))
    axes1[i - 8].set_ylabel('Координата y')
    axes1[i - 8].set_xlabel('Координата x')
    axes1[i - 8].set_zlabel('U(x,t)')

    axes2.append(figurs[i - 8].add_subplot(1, 3, 2, projection='3d'))
    axes2[i - 8].set_title('Аналитическое решение в момент\n времени t = ' + str(Arr[i]))
    axes2[i - 8].set_ylabel('Координата y')
    axes2[i - 8].set_xlabel('Координата x')
    axes2[i - 8].set_zlabel('U(x,t)')

    axes3.append(figurs[i - 8].add_subplot(1, 3, 3, projection='3d'))
    axes3[i - 8].set_title('Разница между численым и аналитическим решение\n в момент времени t = ' + str(Arr[i]))
    axes3[i - 8].set_ylabel('Координата y')
    axes3[i - 8].set_xlabel('Координата x')
    axes3[i - 8].set_zlabel('U(x,t)')


f.close()

f = open('data\\x.txt')

X = []

for x in f:
    X.append(float(x))

f.close()

f = open('data\\y.txt')

Y = []

for y in f:
    Y.append(float(y))

gx = np.ravel(X)
gy = np.ravel(Y)

f.close()

count = 0
for name in names:
    f = open(name + ".txt")
    a = open(name + "_a.txt")
    d = open(name + "_d.txt")
    Arr = []
    AArr = []
    DArr = []
    # mas = f.read()
    # mas.split("\n")
    for x in f:
        Arr.append(float(x))  
    for x in a:
        AArr.append(float(x))
    for x in d:
        DArr.append(float(x)) 
    axes1[count].plot_trisurf(X, Y, Arr, cmap=cm.jet, edgecolor='none')
    axes2[count].plot_trisurf(X, Y, AArr, cmap=cm.jet, edgecolor='none')
    axes3[count].plot_trisurf(X, Y, DArr, cmap=cm.jet, edgecolor='none')
    count += 1
    f.close()

plt.show()