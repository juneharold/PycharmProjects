# DO NOT EDIT THIS CODE!
import os
import pandas as pd
import numpy as np
from collections import Counter


def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts


def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


# Exercise 1
hamlets = pd.read_csv("/UPFR/hamlets.csv", index_col=0)
"""print(hamlets)"""


# Exercise 2
language, text = hamlets.iloc[0]
counted_words = count_words_fast(text)
"""print(counted_words["hamlet"])"""

"""data = pd.DataFrame(columns=("word", "count"))
for i in range(0, len(counted_words)):
    word = list((counted_words.keys()))[i]
    count = counted_words[list((counted_words.keys()))[i]]
    data.loc[i] = word, count"""


# Exercise 3
"""data = pd.DataFrame(columns=("word", "count", "length", "frequency"))
number_of_unique_words = 0

for i in range(0, len(counted_words)):
    word = list((counted_words.keys()))[i]
    count = counted_words[list((counted_words.keys()))[i]]
    length = len(list((counted_words.keys()))[i])
    if count > 10:
        frequency = "frequent"
    elif 1 < count <= 10:
        frequency = "infrequent"
    else:
        frequency = "unique"
        number_of_unique_words += 1
    data.loc[i] = word, count, length, frequency

print(number_of_unique_words)"""


# Exercise 4
"""frequent_connected = ""
frequent_words = 0
infrequent_words = 0
infrequent_connected = ""
unique_words = 0
unique_connected = ""

sub_data = pd.DataFrame(columns=("language", "frequency", "mean_word_length", "num_words"))
for i in range(0, len(counted_words)):
    word = list((counted_words.keys()))[i]
    count = counted_words[list((counted_words.keys()))[i]]
    frequency = ["frequent", "infrequent", "unique"]
    if count > 10:
        frequent_connected += word
        frequent_words += 1
    elif 1 < count <= 10:
        infrequent_connected += word
        infrequent_words += 1
    else:
        unique_connected += word
        unique_words += 1

sub_data.loc[0] = language, "frequent",  len(frequent_connected)/frequent_words, frequent_words
sub_data.loc[1] = language, "infrequent",  len(infrequent_connected)/infrequent_words, infrequent_words
sub_data.loc[2] = language, "unique",  len(unique_connected)/unique_words, unique_words

print(sub_data)"""


# Exercise 5
def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10, "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1, "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent", "infrequent", "unique"],
        "mean_word_length": data.groupby(by="frequency")["length"].mean(),
        "num_words": data.groupby(by="frequency").size()
    })

    return (sub_data)


final = []
grouped_data = pd.DataFrame(columns=("language", "frequency", "mean_word_length", "num_words"))
for i in range(0, 3):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    final.append(sub_data)

result = pd.concat(final)


# Exercise 6
colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
# write your code to display the plot here!
plt.plot(result.mean_word_length, result.num_words)

