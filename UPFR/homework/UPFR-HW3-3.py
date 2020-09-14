# DO NOT EDIT
import numpy as np
import random
import scipy.stats as ss
import pandas as pd


def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode


def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))


def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]


# Exercise 1
# The questions on the website referring to data means wine_data.
wine_data = pd.read_csv("/UPFR/homework/wine_data.csv", )


# Exercise 2
numeric_data = wine_data.rename(columns={"color": "is_red"})
cleanup = {"red": 1,
           "white": 0}
numeric_data = numeric_data.replace(cleanup)
numeric_data = numeric_data.drop(["is_red", "quality", "high_quality"], axis=1)


# Exercise 3
import sklearn.preprocessing
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns=numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)


# Exercise 4
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:, 0]
y = principal_components[:, 1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha=0.2,
    c=wine_data['high_quality'], cmap=observation_colormap, edgecolors='none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()


# Exercise 5
import numpy as np
np.random.seed(1) # do not change

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)


def accuracy(predictions, outcomes):
    result = []
    if len(predictions) == len(outcomes):
        for i in range(0, len(predictions)):
            if predictions[i] == outcomes[i]:
                result.append(True)
            else:
                result.append(False)
    return (result.count(True) / len(result)) * 100


# Exercise 6
list_of_zero = []
for i in range(0, 6497):
    list_of_zero.append(0)
accuracy(list_of_zero, wine_data["high_quality"])


# Exercise 7
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, wine_data['high_quality'])

library_predictions = knn.predict(numeric_data)
accuracy(library_predictions, wine_data["high_quality"])


# Exercise 8
random.seed(123)
n_rows = wine_data.shape[0]

selection = random.sample(range(n_rows), 10)

# Exercise 9
predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(wine_data["high_quality"])

raise NotImplementedError

my_predictions = []
percentage = accuracy(my_predictions, wine_data.high_quality.iloc[selection])

for p in predictors:
    my_predictions.append(knn_predict(p, predictors[training_indices, :], outcomes[training_indices], k=5))













