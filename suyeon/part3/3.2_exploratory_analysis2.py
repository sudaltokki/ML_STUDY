# -*- coding: utf-8 -*-

import pandas as pd


df = pd.read_csv('./auto-mpg.csv', header=None)


df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인 
print(df.count())
print('\n')

# df.count()가 반환하는 객체 타입: Series 객체
print(type(df.count()))
print('\n')

# .value_counts: 데이터프레임 df의 특정 열이 가지고 있는 고유값 개수 확인
unique_values = df['origin'].value_counts() 
print(unique_values)
print('\n')

# value_counts 메소드가 반환하는 객체 타입 : series
print(type(unique_values))