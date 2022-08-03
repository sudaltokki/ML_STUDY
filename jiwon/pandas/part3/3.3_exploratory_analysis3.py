# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 평균값
print(df.mean())
print('\n')
print(df['mpg'].mean())
print('\n')
print(df.mpg.mean())
print('\n')
print(df[['mpg', 'weight']].mean())

# 중간값
print(df.median())
print('\n')
print(df['mpg'].median())
print('\n')

# 최대값
# 문자열 데이터를 가진 열에 대해서는 문자열을 ASCII 숫자로 변환하여 비교한다.
print(df.max())
print('\n')
print(df['mpg'].max())
print('\n')

# 최소값
print(df.min())
print('\n')
print(df['mpg'].min())
print('\n')

'''
'horsepower' 열은 '?'문자가 포함되어 있기 때문에 다른 숫자 값까지 전부 문자열로 인식된다.
'horsepower' 열의 숫자 크기를 비교해야 한다면 '?'문자를 제거하거나 적절한 숫자로 바꾸고
문자열로 지정되어 있는 값을 숫자형 데이터로 변환해야 하낟.
'''

# 표준편차
# 문자열 데이터를 가진 열에 대해서는 계산하지 않는다.
print(df.std())
print('\n')
print(df['mpg'].std())
print('\n')

# 상관계수
# 산술 데이터를 갖는 모든 열에 대해 2개씩 서로 짝을 짓고, 각각의 경우에 대해 상관계수 계산
# 문자열 데이터를 가진 열은 계산이 불가능하기 때문에 포함하지 않는다.
print(df.corr())
print('\n')
print(df[['mpg', 'weight']].corr())

# 상관계수는 어떨 때 구하며, 어떻게 계산할까?