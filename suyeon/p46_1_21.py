# -*- coding: utf-8 -*-
"""
p46, 1-21
"""
import pandas as pd

student1=pd.Series({'국어':100, '영어':80,'수학':90})

print(student1)
print('\n')

percentage=student1/200
"""c++과 달리, 자동으로 자료형 설정"""

print(percentage)
print('\n')
print(type(percentage))

