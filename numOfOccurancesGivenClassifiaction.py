import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn
import joblib

with open('dataset.pkl', 'rb') as file:
    df = joblib.load(file)
print(type(df))

causeCol = df["STAT_CAUSE_DESCR"]
severityCol = df ["FIRE_SIZE_CLASS"]
doyCol = df["DISCOVERY_DOY"]


def severityBreakdown(let, data):

    classAdata = []
    classBdata = []
    classCdata = []
    classDdata = []
    classEdata = []
    classFdata = []
    classGdata = []

    for i in range(len(severityCol)):

        if severityCol.iloc[i] == 'A':
            classAdata.append(data[i])

        elif severityCol.iloc[i] == 'B':
            classBdata.append(data[i])

        elif severityCol.iloc[i] == 'C':
            classCdata.append(data[i])

        elif severityCol.iloc[i] == 'D':
            classDdata.append(data[i])

        elif severityCol.iloc[i] == 'E':
            classEdata.append(data[i])

        elif severityCol.iloc[i] == 'F':
            classFdata.append(data[i])

        elif severityCol.iloc[i] == 'G':
            classGdata.append(data[i])

    if let == 'A':
        return classAdata

    elif let == 'B':
        return classBdata

    elif let == 'C':
        return classCdata

    elif let == 'D':
        return classDdata

    elif let == 'E':
        return classEdata

    elif let == 'F':
        return classFdata

    elif let == 'G':
        return classGdata


def mostCommonVal(column):
    counts = column.value_counts()
    print(counts)
    return(counts)

def count_elements(lst):
    element_count = {}

    for element in lst:

        if element not in element_count:
            element_count[element] = 1

        else:
            element_count[element] += 1

    return element_count


elements = count_elements(severityBreakdown('G', doyCol))
x = []
y = []

for key in elements:
    x.append(key)
    y.append(elements[key])

print(x)
print(y)
plt.scatter(x, y)
plt.show()
