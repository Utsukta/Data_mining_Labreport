import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

x = [6, 15, 17, 5, 9, 10, 4 , 16, 1, 11]
y = [23, 20, 18, 10, 15, 22, 25, 19, 18, 22]

data = list(zip(x, y))

linkage_data = linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)

plt.show()