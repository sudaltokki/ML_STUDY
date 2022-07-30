# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:30:45 2022

@author: user
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]
df['ten'] = 10
print(df.head())

def add_10(n):
    return n+10

def add_two_obj(a,b):
    return a + b

print(add_10(10))
print(add_two_obj(10,10))

srl = df['age'].apply(add_10)
print(srl.head())
print('\n')

sr2 = df['age'].apply(add_two_obj, b=10)
print(sr2.head())
print('\n')

sr3 = df['age'].apply(lambda x:add_10(x))
print(sr3.head())