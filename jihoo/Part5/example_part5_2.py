# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:14:20 2022

@author: user
"""

import seaborn as sns

df = sns.load_dataset('titanic')

missing_df = df.isnull()
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()
    
    try:
        print(col, ': ', missing_count[True])
    except:
        print(col, ': ', 0)
        
df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns)

df_age = df.dropna(subset = ['age'], how = 'any', axis =0)
print(len(df_age))
