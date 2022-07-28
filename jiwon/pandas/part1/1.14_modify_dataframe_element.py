# -*- coding: utf-8 -*-

import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
print(df)
print('\n')

# 데이터프레임 df의 특정 원소를 변경하는 방법
df.iloc[0][3] = 80
print(df)
print('\n')

df.iloc[0,3] = 100
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)
print('\n')

# 데이터프레임 df의 원소 여러 개를 변경하는 방법
df.loc['서준', ['음악', '체육']] = 50
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = [80, 80]
print(df)
print('\n')