# -*- coding: utf-8 -*-

import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 데이터프레임 df에 '국어' 점수 열(column) 추가. 데이터 값은 80으로 지정
df['국어'] = 80
print(df)