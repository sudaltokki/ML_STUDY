# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 03:45:54 2022

@author: user
"""

import pandas as pd

df = pd.read_csv('C:\\Python_exfiles\\part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df.plot(x='weight', y = 'mpg', kind = 'scatter')