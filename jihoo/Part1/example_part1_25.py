# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:17:31 2022

@author: user
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head()) #첫 5행만 표시
print('\n')
print(type(df))
print('\n')

addition = df + 10
print(addition.head())
print('\n')
print(type(addition))