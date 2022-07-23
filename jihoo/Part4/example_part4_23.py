# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 06:34:43 2022

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('C:\\Python_exfiles\\part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df['count'] = 1
df_origin = df.groupby('origin').sum()
print(df_origin.head())

df_origin.index = ['USA', 'EU', 'JPN']

df_origin['count'].plot(kind = 'pie',  figsize = (7,5), 
                        autopct = '%1.1f%%', startangle = 10,
                        colors = ['chocolate', 'bisque', 'cadetblue'])

plt.title('Model Origin', size = 20)
plt.axis('equal')
plt.legend(labels=df_origin.index, loc='upper right')
plt.show()