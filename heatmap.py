import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px

import datasetAnalysis


dataFrame = datasetAnalysis.df

dataFrameDensity = dataFrame['FIRE_SIZE']
dataFrameDensity = dataFrameDensity.pow(2)

fig = px.density_mapbox(dataFrame, lat = 'LATITUDE', lon = "LONGITUDE", z = 'FIRE_SIZE', center = dict(lat=dataFrame.LATITUDE.mean(),lon=dataFrame.LONGITUDE.mean()),zoom=4,mapbox_style="carto-positron",height=900)
fig.show()


