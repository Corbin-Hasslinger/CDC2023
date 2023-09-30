import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px

import datasetAnalysis


dataFrame = datasetAnalysis.df

# dataFrame = dataFrame.drop(dataFrame[dataFrame['FIRE_SIZE_CLASS'] == 'A'].index)
# dataFrame = dataFrame.drop(dataFrame[dataFrame['FIRE_SIZE_CLASS'] == 'B'].index)
# dataFrame = dataFrame.drop(dataFrame[dataFrame['FIRE_SIZE_CLASS'] == 'C'].index)
# dataFrame = dataFrame.drop(dataFrame[dataFrame['FIRE_SIZE_CLASS'] == 'D'].index)
dataFrame = dataFrame.drop(dataFrame[dataFrame['FIRE_SIZE_CLASS'] == 'E'].index)
dataFrame = dataFrame.drop(dataFrame[dataFrame['FIRE_SIZE_CLASS'] == 'F'].index)
dataFrame = dataFrame.drop(dataFrame[dataFrame['FIRE_SIZE_CLASS'] != 'G'].index)


#Heat Map
fig = px.density_mapbox(dataFrame, 
                        lat = 'LATITUDE', 
                        lon = "LONGITUDE", 
                        z = 'FIRE_SIZE', 
                        radius=30,
                        opacity=0.75,
                        color_continuous_scale='Jet',
                        center = dict(lat=dataFrame.LATITUDE.mean(),lon=dataFrame.LONGITUDE.mean()),
                        zoom=3,
                        mapbox_style="stamen-toner",
                        height=900)

fig.show()


