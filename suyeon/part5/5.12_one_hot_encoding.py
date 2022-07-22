# -*- coding: utf-8 -*-
#5-12 . 원핫인코딩 by sklearn liabrary
#line 33

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환

# np.histogram 으로 3개의 bin으로 나누는 경계 값의 리스트 구하기
count, bin_dividers = np.histogram(df['horsepower'], bins=3)

# 3개의 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

# pd.cut 으로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],     # 데이터 배열
                      bins=bin_dividers,      # 경계 값 리스트
                      labels=bin_names,       # bin 이름
                      include_lowest=True)    # 첫 경계값 포함

# sklern 라이브러리 불러오기
from sklearn import preprocessing    

# 전처리를 위한 encoder 객체 만들기
label_encoder = preprocessing.LabelEncoder()       # label encoder 생성
#주로 1d array(Series) 에 사용

onehot_encoder = preprocessing.OneHotEncoder()   # one hot encoder 생성
#반드시 2d array(dataFrame)을 사용

# label encoder로 문자열 범주를 숫자형 범주로 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))  
print(onehot_labeled)
print(type(onehot_labeled))

#.fit_transform() : fit(정규화; 최대 최소 인지, 평균 편차 계산) 후에 
#transform(train data)의 최소값은 0, 최대값은 1로 맵핑:  one hot encoding
#https://wpaud16.tistory.com/148

# 2차원 행렬로 형태 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1) #1: 변경할 차원
print(onehot_reshaped)
print(type(onehot_reshaped))
#np.reshape() : 원하는 행*열의 ndarray 반환
#https://yganalyst.github.io/data_handling/memo_5/


# 희소행렬로 변환
#희소행렬 : 희소행렬(sparse matrix)은 행렬의 값이 대부분 0인 경우를 가리키는 표현이다. 그와 반대되는 표현으로는 밀집행렬(dense matrix), 조밀행렬이 사용된다. 개념적으로 희소성은 시스템들이 약하게 연결된 것에 해당한다.
# (행, 열) 좌표    값    형태로 정리

onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))



#https://datamasters.co.kr/78



