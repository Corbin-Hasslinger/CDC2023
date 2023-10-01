import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import joblib

with open('dataset.pkl', 'rb') as file:
    df = joblib.load(file)

dataFrame = df

dataFrame.drop(df.index[df.index > 10], inplace=True)

print(dataFrame)
