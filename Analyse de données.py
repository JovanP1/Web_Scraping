import os
os.getcwd()
os.chdir("C:\\Users\\mehdi\\Desktop\\M1 ecotr\\Langage de programmation 1\\Web scraping\\csv files")
import pandas as pd


brands = pd.read_csv("Brands.csv",sep=";")


from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
 

brands = brands.set_index('Marque')
del brands.index.name

Z = linkage(brands, 'ward')

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance (Ward)')
dendrogram(Z, labels=brands.index, leaf_rotation=90)
plt.savefig('C:\\Users\\mehdi\\Desktop\\M1 ecotr\\Langage de programmation 1\\Web scraping\\csv files\\Dendrogram.eps', format='eps')
