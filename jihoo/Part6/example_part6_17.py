# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 01:31:14 2022

@author: user
"""
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

grouped_filter = grouped.filter(lambda x : len(x) >= 200)
print(grouped_filter.head())
print('\n')
print(type(grouped_filter))

age_filter = grouped.filter(lambda x : x.age.mean() < 30)
print(age_filter.tail())
print('\n')
print(type(age_filter))