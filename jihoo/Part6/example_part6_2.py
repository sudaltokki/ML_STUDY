# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:38:50 2022

@author: user
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]
print(df.head())

def add_10(n):
    return n+10

df_map = df.applymap(add_10)
print(df_map.head())