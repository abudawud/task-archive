# Metode Grafik - Cara Grafix
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 2, 0.001)
f1 = 2 * (x**3)             # f(x) = 2x^3
f2 = ((2 * x) + 1)**3       # f(x) = (2x + 1)^3

x1 = np.arange(-15, 15, 0.01)
y1 = 0 * x1

y2 = np.arange(-15, 15, 0.01)
x2 = 0 * y2

plt.axes(aspect='equal')
plt.plot(x1, y1, c='k', ls='--')
plt.plot(x2, y2, c='k', ls='--')
plt.plot(x, f1, label="$\mathregular{f(x) = 2x^3}$")
plt.plot(x, f2, label="$\mathregular{f(x) = (2x + 1)^3}$")
plt.text(0.8, 0.6, 'akar', fontsize='15')

plt.ylim(top=15, bottom=-15)
plt.xlim(right=15, left=-15)
plt.title('Grafik Ganda')
plt.legend()
plt.grid()
plt.show()