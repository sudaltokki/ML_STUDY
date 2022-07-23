# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:39:10 2022

@author: user
"""

import pandas as pd

student1 = pd.Series({'국어' : 100, '영어': 80, '수학':90})
print(student1)
print('\n')

percentage = student1/200

print(percentage)
print('\n')
print(type(percentage))