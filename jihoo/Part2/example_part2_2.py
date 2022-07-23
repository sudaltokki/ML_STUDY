# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:43:55 2022

@author: user
"""

import pandas as pd

df1 = pd.read_excel('C:\\Python_exfiles\\part2/남북한발전전력량.xlsx', engine= 'openpyxl')

df2 = pd.read_excel('C:\\Python_exfiles\\part2/남북한발전전력량.xlsx', 
                    engine= 'openpyxl', header = None)

print(df1)
print('\n')
print(df2)