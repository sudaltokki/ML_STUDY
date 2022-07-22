# -*- coding: utf-8 -*-
#4-2) 더미 변수
#카테고리를 나타내는 범주형 데이터를 회귀 분석 등 머신러닝 알고리즘에 바로 사용할 수 없는 경우에는 컴퓨터가 인식 가능한 입력값으로 변환해야 함
#즉 카테고리형 데이터를 0또는 1로 표현되는 더미 변수를 사용해서 나타냄.
# 어떤 특성의 여부 표현. 어떤 특성 존재 시 1, 존재하지 않을 시 0
#one-hot-encoding; one-hot vector(0또는 1)로 변환

#5-11. 더미 변수
#line 38

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

# hp_bin 열의 범주형 데이터를 더미 변수로 변환
horsepower_dummies = pd.get_dummies(df['hp_bin'])
#pd.get_dummies(): 범주형 변수의 모든 고유값을 각각 새로운 더미 변수로 변환
# 고유값 n개가 각각 새로운 더미 변수 열의 이름이 되어, 각 더미 변수가 원래 속한 행은 1, 아니면 0으로 입력
#n열의 새 데이터프레임 반환

#변수별 자료형 등 확인하고 싶을 때 print type하지 말고, 오른쪽의 Variable Explorer로 바로 확인 가능


print(horsepower_dummies.head(15))
