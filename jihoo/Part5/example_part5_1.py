# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:06:57 2022

@author: user
"""

import seaborn as sns

df = sns.load_dataset('titanic')

nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)
print(df.head().isnull())
print(df.head().notnull())

print(df.head().isnull().sum(axis=0))