# Q1  : Analyse the data and give a suggestion of type of machine learning system that can be applied.
# Ans : Untuk mendapatkan fitur yang lebih penting dalam menentukan harga kita dapat menggunakan unsupervised machine learning.

# Q2  : - Find min or max of a value
#       - Eliminate null value
#       - Replace null value to certain value

import pandas as pd
dataset = pd.read_csv('listings.csv')

# --------Find min/max---------
value = input('Input which value to find the min and max : ')
print('Max ' + value + ' : ' + str(dataset[value].max()))
print('Min ' + value + ' : ' + str(dataset[value].min()))


# ---------Eliminate null value-------
newDataset = dataset.dropna()
# print(newDataset.isna().values.any())



# ---------Replace null value to certain value---------
value2 = input('Input null replacement : ')
newDataset2 = dataset.fillna(value2)
