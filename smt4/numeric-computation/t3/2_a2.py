# Metode Grafik - Cara Grafix
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-0.1, 2.5, 0.01)
f1 = np.exp(-x)
f2 = x

x1 = np.arange(-0.2, 2.5, 0.01)
y1 = 0 * x1

y2 = np.arange(-0.2, 1.5, 0.01)
x2 = 0 * y2

plt.plot(x, f1, label="f(x) = exp(-x)")
plt.plot(x, f2, label="f(x) = x")
plt.plot(x1, y1, c='r')
plt.plot(x2, y2, c='r')
plt.text(0.8, 0.6, 'akar', fontsize='15')
plt.ylim(top=1.5)

plt.title('Grafik Ganda')
plt.legend()
plt.show()