# Metode Grafik - Cara Grafix
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-0.1, 0.67, 0.01)
f = np.exp(-x) - x

x1 = np.arange(-0.2, 1.5, 0.01)
y1 = 0 * x1

y2 = np.arange(-0.2, 1.5, 0.01)
x2 = 0 * y2

plt.plot(x, f, label="f(x) = exp(-x) - x")
plt.plot(x1, y1, c='r')
plt.plot(x2, y2, c='r')
plt.text(0.6, 0.08, 'akar', fontsize='15')

plt.title('Grafik Tunggal')
plt.legend()
plt.show()