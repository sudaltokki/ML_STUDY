# -*- coding: utf-8 -*-

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터프레임 df의 내용 미리보기
print(df.head())     # 처음 5개의 행
print('\n')
print(df.tail())     # 마지막 5개의 행

# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환 
print(df.shape)
print('\n')

# 데이터프레임 df의 기본 정보
print(df.info())
print('\n')

# 데이터프레임 df의 각각의 열의 자료형 확인 
print(df.dtypes)
print('\n')

# 시리즈(mog 열)의 자료형 확인 
print(df.mpg.dtypes) #df['mpg'].dtypes
print('\n')

# 데이터프레임 df의 기술통계 정보 확인 
print(df.describe())
print('\n')
print(df.describe(include='all'))#산술데이터 아닌 열에 대한  정보: 고유값 개수, 최빈값, 빈도수/ 산술데이터 열은 NaN