# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 23:53:37 2022

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

df.to_csv("./df_sample.csv")