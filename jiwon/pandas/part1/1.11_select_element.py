# -*- coding: utf-8 -*-

import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경 사항 반영
df.set_index('이름', inplace=True)
print(df)
print('\n')

# 데이터프레임 df의 특정 원소 1개 선택
a = df.loc['서준', '음악']
print(a)
b = df.iloc[0, 2]
print(b)
print('\n')

# 데이터프레임 df의 특정 원소 2개 이상 선택
c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0, [2, 3]]
print(d)
e = df.loc['서준', '음악':'체육'] # 범위를 지정할때는 대괄호에 넣지 않는다 ['음악':'체육'](x)
print(e)
f = df.iloc[0, 2:]
print(f)

# loc에서는 인덱스 이름의 범위를 지정할 때는 범위의 끝이 포함되지만, iloc에서는 범위의 끝을 제외하고 선택한다. 