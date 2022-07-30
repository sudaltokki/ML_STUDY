# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:58:38 2022

@author: user
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]
print(df.head())
print('\n')

def missing_value(series):
    return series.isnull()

result = df.apply(missing_value,axis=0)
print(result.head())
print('\n')
print(type(result))