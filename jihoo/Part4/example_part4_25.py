# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 06:44:06 2022

@author: user
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.head())
print('\n')
print(titanic.info())

