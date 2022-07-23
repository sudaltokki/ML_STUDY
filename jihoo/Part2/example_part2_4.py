# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:51:43 2022

@author: user
"""

import pandas as pd

url = 'C:\\Python_exfiles\\part2/sample.html'

tables = pd.read_html(url)

print(len(tables))
print('\n')

for i in range(len(tables)):
    print("tables[%s]"%i)
    print(tables[i])
    print('\n')
    
df = tables[1]

df.set_index(['name'], inplace = True)
print(df)