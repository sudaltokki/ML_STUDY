# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacemnet', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 데이터프레임 내용을 일부 확인
print(df.head())
print('\n')
print(df.tail())

# 데이터프레임의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환
print(df.shape)
print('\n')

'''
데이터프레임의 기본 정보 확인
데이터프레임의 클래스 유형, 행 인덱스와 열에 관한 정보(열의 이름, 데이터 개수, 자료형), 
자료형과 메모리 사용량 표시

판다스는 Numpy를 기반으로 만들어졌기 때문에 Numpy에서 사용하는 자료형을 기본적으로 사용할 수 있다.
파이썬의 기본 자료형과 비슷하지만 시간을 나타내는 datetime64와 같은 자료형이 있다는 점에서 일부 차이가 있다.
'''
print(df.info())
print('\n')

# 데이터프레임의 자료형 확인
print(df.dtypes)
print('\n')

# 특정 열의 자료형 확인
print(df.mpg.dtypes)

'''
데이터프레임의 기술 통계 정보 확인
describe() 메소드를 적용하면 산술 데이터를 갖는 열에 대한 주요 기술 통계정보를 요약해 출력한다
ex. 평균, 표준편차, 최대값, 최소값, 중간값 등

산술 데이터가 아닌 열에 대한 정보를 포함하고 싶을 때는 include='all' 옵션을 추가한다.
산술 데이터가 아닌 열에 대해서는 unique(고유값 개수), top(최빈값), freq(빈도수)에 대한 정보를 제공한다.
'''
print(df.describe())
print('\n')
print(df.describe(include='all'))