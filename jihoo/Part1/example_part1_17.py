# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:21:46 2022

@author: user
"""

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')


#{}는 딕셔너리에서(짝지어주기), 일반적인 array에서는 []쓰면됨
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print('\n')

ndf2 = df.reindex(new_index, fill_value = 0)
print(ndf2)