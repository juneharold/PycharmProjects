import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5

plt.plot(x, y1, "bo-", linewidth=2, markersize=12, label="First")
plt.plot(x, y2, "gs-", linewidth=2, markersize=12, label="Second")
plt.xlabel("X")
plt.xlabel("Y")
plt.axis([-0.5, 10.5, -5, 105])  # [xmin, xmax, ymin, ymax]
plt.legend(loc="upper left")
plt.savefig("LOL.jpg")