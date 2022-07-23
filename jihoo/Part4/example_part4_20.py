# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 06:23:16 2022

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('C:\\Python_exfiles\\part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df.plot(kind = 'scatter',x = 'weight', y = 'mpg', c = 'coral', s=10, figsize = (10,5))
plt.title('Scatter Plot - mpg vs weight')
plt.show()