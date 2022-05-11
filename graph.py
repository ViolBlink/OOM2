import numpy as np
import matplotlib.pyplot as plt

f = open('Config.txt')

Arr = f.read()
Arr = Arr.split("\n")

N = int(Arr[0].split(" ")[2])

hx = np.pi/3/(N - 1)

J = int(Arr[1].split(" ")[2])

f.close()

""" Численый счет """

f = open('Data.txt')

Lattis = np.zeros((J + 1, N + 1))
Arr = []

for x in f:
    Arr.append(float(x))

count = 0

for j in range(N):
    for q in range(J):
        Lattis[j][q] = Arr[count]
        count = count + 1

X = np.linspace(-hx/2, np.pi/3 + hx/2, N + 1)
Y = np.linspace(0, np.pi/2, J + 1)

gx, gt = np.meshgrid(X, Y)

fig3 = plt.figure(figsize=(10, 10))
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot_surface(gx, gt, Lattis, rstride=10,cstride=10)
ax3.set_title('Численное решение')
ax3.set_ylabel('Координата y')
ax3.set_xlabel('Координата x')
ax3.set_zlabel('U(x,t)')

plt.show()