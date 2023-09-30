import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# generating 2-D 10x10 matrix of random numbers
# from 1 to 100
data = np.random.randint(low = 1,
                         high = 100,
                         size = (10, 10))
print("The data to be plotted:\n")
print(data)
  
# plotting the heatmap
hm = sns.heatmap(data = data)
  
# displaying the plotted heatmap
plt.show()