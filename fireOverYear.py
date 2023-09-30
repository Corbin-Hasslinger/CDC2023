import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

import datasetAnalysis

dataframe = datasetAnalysis.df[['FIRE_YEAR','FIRE_SIZE']].sample(n=500000)
print(dataframe.head())

sns.set_theme(style="darkgrid")

sns.displot(dataframe, x='FIRE_YEAR', discrete=True,rug=True)



plt.xlabel("Year")
plt.ylabel("Number of Fires")
plt.yticks([])

plt.show() 




