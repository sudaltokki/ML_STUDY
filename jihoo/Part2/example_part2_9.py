# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 00:01:33 2022

@author: user
"""

import pandas as pd

data = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ["A+","A+", "B"], 
        'basic' : ["A", "A+", "B"],
        'C++' : ["B+", "C", "C+"]}

df = pd.DataFrame(data)
df.set_index('name', inplace = True)
print(df)

df.to_excel("./df_sample.xlsx")