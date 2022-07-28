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

# 데이터프레임 df를 전치하기(메소드 활용)
df = df.transpose()
print(df)
print('\n')

# 데이터프레임 df를 다시 전치하기(클래스 속성 활용)
df = df.T
print(df)

'''
전치의 결과로 새로운 객체를 반환하므로 
기존 객체를 변경하기 위해서는 df = df.transpose() 또는 df = df.T 와 같이
기존 객체에 새로운 객체를 할당해주는 과정이 필요하다.
'''