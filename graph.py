import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



f = open('Config.txt')

Arr = f.read()
Arr = Arr.split("\n")

""" Считываем параметры """
Nx = int(Arr[0].split(" ")[2]) # Считывем Nx

Ny = int(Arr[1].split(" ")[2]) # Считывем Ny

T = []

for i in range(8, len(Arr)):
    T.append(int(Arr[i]))

f.close()

""" Считываем данные """

f = open('Data.txt')

Lattis = np.zeros((Nx + 1, Ny + 1))
Arr = []

for x in f:
    Arr.append(float(x))

# count = 0

# for j in range(Nx):
#     for q in range(Ny):
#         Lattis[j][q] = Arr[count]
#         count = count + 1

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

# X = np.linspace(-(np.pi)/(2*(Nx - 1)), np.pi/3, Nx + 1)
# Y = np.linspace(0, np.pi/2, Ny + 1)

gx = np.ravel(X)
gy = np.ravel(Y)

# theta = 2 * np.pi * np.random.random(1000)

# r = 6 * np.random.random(1000)
# x = np.ravel(r * np.sin(theta))
# y = np.ravel(r * np.cos(theta))

# z = np.sin(np.sqrt(x ** 2 + y ** 2))

# ax = plt.axes(projection='3d')
# ax.plot_trisurf(x, y, z,
#                 cmap='viridis', edgecolor='none')

fig1 = plt.figure(figsize=(110, 110))
ax1 = fig1.add_subplot(projection='3d')
ax1.plot_trisurf(X, Y, Arr, cmap=cm.jet, edgecolor='none')
ax1.set_title('Численное решение')
ax1.set_ylabel('Координата y')
ax1.set_xlabel('Координата x')
ax1.set_zlabel('U(x,t)')

plt.show()