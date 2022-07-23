# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:29:57 2022

@author: user
"""

import seaborn as sns

df = sns.load_dataset('titanic')

print(df['embark_town'][825:830])
print('\n')

df['embark_town'].fillna(method = 'ffill', inplace=True)

print(df['embark_town'][825:830])