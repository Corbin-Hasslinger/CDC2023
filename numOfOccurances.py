import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

import joblib

with open('dataset.pkl', 'rb') as file:
    df = joblib.load(file)

causeCol = df["STAT_CAUSE_DESCR"]
severityCol = df ["FIRE_SIZE_CLASS"]

data = []

for i in range(len(causeCol)):
    data.append(causeCol[i])

def count_elements(lst):
    element_count = {}

    for element in lst:

        if element not in element_count:
            element_count[element] = 1

        else:
            element_count[element] += 1

    return element_count


x = []
y = []

elements = count_elements(data)

for key in elements:
    x.append(key)
    y.append(elements[key])

plt.scatter(x, y)
plt.show()
