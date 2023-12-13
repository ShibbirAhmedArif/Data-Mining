# -*- coding: utf-8 -*-
"""Find the final three clusters using KMeans Algorithm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T9biS1LjeLj0MX9EsZGg6zd1sVFutORr
"""

from sklearn.cluster import KMeans
import numpy as np

# create a numpy array to define the data points
data = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])

# Initialize cluster centers
initial_centers = np.array([[2, 10], [5, 8], [1, 2]])

# Create a KMeans model with 3 clusters
kmeans = KMeans(n_clusters=3, init=initial_centers, n_init=1, random_state=0)

# Fit the model
kmeans.fit(data)

# Print the final three clusters
print("The final three clusters:")
print(kmeans.cluster_centers_)