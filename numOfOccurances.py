import pandas as pd
import numpy as np
import matplotlib as plt

import joblib

with open('dataset.pkl', 'rb') as file:
    df = joblib.load(file)
print(type(df))

causeCol = df[["STAT_CAUSE_DESCR"]]
severityCol = df [["FIRE_SIZE_CLASS"]]

def mostCommonVal(column):
    counts = column.value_counts()
    print(counts)
    return(counts)


mostCommonVal(causeCol)
