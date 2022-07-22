# -*- coding: utf-8 -*-
#3-2) 자료형 변환
#5-9. 자료형 변환


# 라이브러리 불러오기
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# 각 열의 자료형 확인
print(df.dtypes)   
print('\n')
#각 변수마다 적절한 자료형을 고려하여 바꿔야할지 판단
#'model year', 'origin 열': 카테고리를 나타내는 범주형이 적절
#범주형 데이터 의미: https://www.ibm.com/docs/ko/spss-statistics/SaaS?topic=variables-simple-tables-categorical


# horsepower 열의 고유값 확인
print(df['horsepower'].unique())
print('\n')
# .unique: 데이터에 존재하는 유일한 값(값의 종류)를 어레이로 반환
#(https://jaaamj.tistory.com/112)

#누락데이터때문에 나머지 숫자 데이터까지 문자열로 인식된 상황


# 누락 데이터('?') 삭제 
import numpy as np
df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
#데이터 대체: df.replace()
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
#Nan데이터 삭제: df.dropna()
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환
#df.astype(): 데이터 타입 변경 
#(https://wikidocs.net/151412)
#.astype과 .map의 차이: https://wikidocs.net/151412  
# astype은 pd 객체를 변경하여 새 객체 생성하므로 더 빠르고, map은 각 데이터 요소마다 자료형 변경하므로 오래걸림

# horsepower 열의 자료형 확인
print(df['horsepower'].dtypes)  
print('\n')

# origin 열의 고유값 확인
print(df['origin'].unique())

# 정수형 데이터를 문자형 데이터로 변환 
df['origin'].replace({1:'USA', 2:'EU', 3:'JAPAN'}, inplace=True)
#replace({1:'USA', 2:'EU', 3:'JAPAN'} ) 문법 확인, 각 요소 별로 변경값 지정하고 싶을 때 
#자동으로 정수형이 object형(문자열 형)으로 변경


# origin 열의 고유값과 자료형 확인
print(df['origin'].unique())
print(df['origin'].dtypes) 
print('\n')

# origin 열의 문자열 자료형을 범주형으로 변환
#유한개의 고유값이 반복적으로 나타나는 경우 범주형(category) 데이터로 변환이 효율적

df['origin'] = df['origin'].astype('category')     
print(df['origin'].dtypes) 

#df.dtypes: df의 각 원소 자체의 데이터형 반환(카테고리형, 정수, 문자열object ---), type( ): 인자 객체의 자료형 반환(df, series, tuple ---)



# 범주형을 문자열로 다시 변환
df['origin'] = df['origin'].astype('str')     
print(df['origin'].dtypes)

# model year 열의 정수형을 범주형으로 변환
print(df['model year'].sample(3))
# df.sample(n) : n개 행을 무작위로 선택

df['model year'] = df['model year'].astype('category') 
#연도는 시간적 순서의 의미는 있으나, 숫자의 상대적 크기는 별 의미가 없으므로, 숫자 형태 이더라도 자료형은 범주형으로 표현하는 게 적절

print(df['model year'].sample(3)) 