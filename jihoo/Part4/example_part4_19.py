# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 06:16:56 2022

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('C:\\Python_exfiles\\part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df['mpg'].plot(kind = 'hist', bins = 10, color = 'coral', figsize = (10,5))

plt.title('Histogram')
plt.xlabel('mpg')
plt.show()