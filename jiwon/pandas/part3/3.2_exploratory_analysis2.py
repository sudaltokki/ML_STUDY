# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']


# 데이터프레임의 각 열이 가지고 있는 원소 개수 확인 - 유효한 값의 개수만을 계산, 시리즈로 반환
print(df.count())
print('\n')

# df.count()가 반환하는 객체 타입 출력
print(type(df.count()))

'''
데이터프레임의 특정 열이 가지고 있는 고유값 확인
value_counts() 메소드로 각 열의 고유값의 종류와 개수를 확인할 수 있다.
고유값이 행 인덱스가 되고, 고유값의 개수가 데이터 값이 되는 시리즈 객체가 만들어진다.
dropna=True 옵션을 설정하면 데이터 값 중에서 NaN을 제외하고 개수를 계산한다.
기본 옵션은 dropna=False

unique() 메소드가 어떤 종류의 데이터 값이 있는지 알려준다면, 
value_counts() 메소드는 각 종류별로 몇 개의 데이터가 있는지 세어준다.
'''
unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')

# value_counts() 메소드가 반환하는 객체 타입 출력
print(type(unique_values))