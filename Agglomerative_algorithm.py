import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

x = [10, 15, 17, 5, 19, 10, 7 , 16, 4, 18]
y = [25, 20, 28, 10, 13, 22, 21, 17, 19, 27]

data = list(zip(x, y))

# Perform Agglomerative Clustering
hierarchical_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

# Use scipy to create a dendrogram
linkage_data = linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()
