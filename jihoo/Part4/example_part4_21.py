# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 06:28:26 2022

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('C:\\Python_exfiles\\part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

cylinders_size = df.cylinders/df.cylinders.max() * 300

df.plot(kind = 'scatter',x = 'weight', y = 'mpg', c = 'coral', figsize = (10,5), 
        s=cylinders_size, alpha = 0.3)
plt.title('Scatter Plot : mpg - weight - cylinders')
plt.show()