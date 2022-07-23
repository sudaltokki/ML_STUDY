# -*- coding: utf-8 -*-

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 평균값 
print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean()) #두개 이상의 열의 평균값을 각각 계산(시리즈로 전달)
print(df[['mpg','weight']].mean())

c=df[['mpg','weight']].mean()
print(c.dtypes) # c.dtypes: float, type(c):  series 두 함수 구분
print(type(c))

# 중간값 
print(df.median())
print('\n')
print(df['mpg'].median())

# 최대값 
print(df.max()) #문자열이 포함된 열은 데이터가 모두 ASCII 숫자로 변환되어 비교(해당 열에 포함된 숫자값도)
print('\n')
print(df['mpg'].max())

# 최소값 
print(df.min())
print('\n')
print(df['mpg'].min())

# 표준편차 
print(df.std())
print('\n')
print(df['mpg'].std())

# 상관계수 
print(df.corr()) #데이터 프레임 반환
print('\n')
print(df[['mpg','weight']].corr())#두개의 열을 따로 선택하여 상관계수 계산, 2*2 df