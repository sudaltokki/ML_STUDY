# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 20:17:44 2022

@author: user
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')

mask1 = (titanic.age >= 10) & (titanic.age < 20)
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head())

mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :]
print(df_female_under10.head())

mask3 = (titanic.age < 10) | (titanic.age >= 60)
df_under10_morethan60 = titanic.loc[mask3,['age','sex','alone']]
print(df_under10_morethan60.head())