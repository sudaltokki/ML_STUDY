# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:32:53 2022

@author: user
"""

import pandas as pd

df = pd.DataFrame({'c1' : ['a', 'a', 'b', 'a', 'b'], 
                   'c2' : [1, 1, 1, 2, 2],
                   'c3' : [1, 1, 2, 2, 2]})
print(df)
print('\n')

df_dup = df.duplicated()
print(df_dup)
print('\n')

col_dup = df['c2'].duplicated()
print(col_dup)
