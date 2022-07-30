# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 19:05:48 2022

@author: user
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]
print(df.head())
print('\n')

def min_max(x):
    return x.max()-x.min()

result = df.apply(min_max)
print(result)
print('\n')
print(type(result))