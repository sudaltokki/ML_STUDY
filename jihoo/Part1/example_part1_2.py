# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 00:54:59 2022

@author: user
"""

import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)
