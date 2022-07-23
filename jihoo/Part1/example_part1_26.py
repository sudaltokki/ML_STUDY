# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:35:18 2022

@author: user
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail()) #마지막 5행만 표시
print('\n')
print(type(df))
print('\n')

addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))
print('\n')

subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))