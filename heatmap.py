import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px

import datasetAnalysis


dataFrame = datasetAnalysis.df

dataFrameDensity = dataFrame['FIRE_SIZE']
dataFrameDensity = dataFrameDensity.pow(2)


#Heat Map
fig = px.density_mapbox(dataFrame, 
                        lat = 'LATITUDE', 
                        lon = "LONGITUDE", 
                        z = 'FIRE_SIZE', 
                        radius=50,
                        opacity=0.75,
                        color_continuous_scale='Jet',
                        center = dict(lat=dataFrame.LATITUDE.mean(),lon=dataFrame.LONGITUDE.mean()),
                        zoom=4,
                        mapbox_style="stamen-toner",
                        height=900)
# Scatter Map Box

fig2 = px.scatter_mapbox(dataFrame.sample(n=5000),
                        lat = 'LATITUDE', 
                        lon = "LONGITUDE", 
                        zoom = 5)


fig.show()


