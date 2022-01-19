from covid import Covid
cases = Covid().get_status_by_country_id(1)
for x in cases:
    print(x, ":", cases[x])

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
print(x)
y = 2*x + 1

plt.plot(x, y)
plt.show()
