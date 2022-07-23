# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:23:32 2022

@author: user
"""

import seaborn as sns

df = sns.load_dataset('titanic')

print(df['embark_town'][825:830])
print('\n')

most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq)
print('\n')

df['embark_town'].fillna(most_freq, inplace=True)

print(df['embark_town'][825:830])