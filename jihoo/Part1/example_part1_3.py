# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 01:05:33 2022

@author: user
"""

import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별','학생여부'])
print(sr)

print(sr[0])
print(sr['이름'])

print(sr[[1,2]])
print('\n')
print(sr[['생년월일', '성별']])

print(sr[1:2])
print('\n')
print(sr['생년월일' : '성별'])
