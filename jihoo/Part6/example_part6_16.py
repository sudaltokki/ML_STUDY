# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 01:20:43 2022

@author: user
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

age_mean = grouped.age.mean()
print(age_mean)
print('\n')

age_std = grouped.age.std()
print(age_std)
print('\n')

for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key])/age_std.loc[key]
    print('* origin :', key)
    print(group_zscore.head(3))
    print('\n')
    
def z_score(x):
    return (x-x.mean())/x.std()

age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1,9,0]])
print('\n')
print(len(age_zscore))
print('\n')
print(age_zscore.loc[0:9])
print('\n')
print(type(age_zscore))