# -*- coding: utf-8 -*-

import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)

# '수학' 점수 데이터만 선택. 변수 math1에 저장
math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

# '영어' 점수 데이터만 선택. 변수 english에 저장
english = df.영어 # '영어'라고 쓰지 않음
print(english)
print(type(english))
print('\n')

# 열 1개만 선택한 경우 시리즈 객체로 반환된다.

# '음악', '체육' 점수 데이터를 선택. 변수 music_gym에 저장
music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

# '수학' 점수 데이터만 선택. 변수 math2에 저장
math2 = df[['수학']]
print(math2)
print(type(math2))
print('\n')
# 열 2개 이상을 선택하거나, 열이 1개라도 2중 대괄호[[]]를 사용하는 경우 데이터프레임 객체로 반환된다.


# 정수 인덱스 범위를 지정하여 열을 선택
print(df.iloc[: : 2])
print('\n')
print(df.iloc[0:3:2])
print('\n')
print(df.iloc[: : -1]) # 역순으로 인덱싱

