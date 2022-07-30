# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 01:51:05 2022

@author: user
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class', 'sex'])

gdf = grouped.mean()
print(gdf)
print('\n')
print(type(gdf))

print(gdf.loc['First'])

print(gdf.loc[('First', 'female')])

print(gdf.xs('male', level = 'sex'))
