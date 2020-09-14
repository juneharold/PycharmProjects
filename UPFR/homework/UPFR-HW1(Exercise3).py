def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    list = []
    for i in range(1, n+1):
        value = (x[i-1] + x[i] + x[i + n_neighbors]) / width
        list.append(value)

    return list


"""x = [0, 10, 5, 3, 1, 5]
print(moving_window_average(x, 1))"""


import random
random.seed(1)

R = 1000
x = []
Y = []

for n in range(R):
    value = random.uniform(0.0, 1.0)
    x.append(value)

Y.append(x)

for i in range(1, 10):
    t = moving_window_average(x, i)
    Y.append(t)

print(Y[5][9])

for i in range(len(Y)):
  print(max(Y[i]) - min(Y[i]))
