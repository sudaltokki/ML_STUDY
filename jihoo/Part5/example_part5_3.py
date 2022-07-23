# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:17:34 2022

@author: user
"""

import seaborn as sns

df = sns.load_dataset('titanic')

print(df['age'].head(10))
print('\n')

mean_age = df['age'].mean(axis=0)
df['age'].fillna(mean_age, inplace=True)

print(df['age'].head(10))
