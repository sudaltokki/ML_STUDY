# -*- coding: utf-8 -*-
#4. 범주형(카테고리) 데이터 처리
#4-1) 구간 분할
#구간 분할: 연속 변수를 일정한 구간으로 나누고, 각 구간을 범주형 이산 변수로 변환하는 과정
#가격, 비용, 효율 등 연속적 값을 수준이나 정도 나타내는 이산적 값으로 나타내어 구간별 차이 나타내면 편리
#pd.cut()


#5-10. 데이터 구간 분할
#line 28부터 참고


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

# np.histogram 함수로 3개의 bin으로 나누는 경계 값의 리스트 구하기
count, bin_dividers = np.histogram(df['horsepower'], bins=3)
#3개의 bin으로 나누는 경우 4개의 경계값 필요함

#np.histogram(data, bins=n): 구간 나눔 (pd.cut 사용 전)
#2개 값 반환: 각 구간에 속하는 값의 개수(count), 경계값 리스트(bin_dividers)
print(bin_dividers) 

# 3개의 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

#pd.cut:  나누어진 데이터를 각 bin에 할당
# pd.cut 함수로 각 데이터를 3개의 bin에 할당한 데이터 열을 새로 생성
df['hp_bin'] = pd.cut(x=df['horsepower'],     # 데이터 배열 선택
                      bins=bin_dividers,      # 경계 값 리스트
                      labels=bin_names,       # bin 이름
                      include_lowest=True)    # 첫 경계값 포함(각 구간의 가장 낮은 경계값 포함)


# horsepower 열, hp_bin 열의 첫 15행을 출력
print(df[['horsepower', 'hp_bin']].head(15))
print(type(df[['horsepower', 'hp_bin']]))
# 여러개 열 동시 선택 시 df[] 안에 리스트[]로 전달-> 데이터프레임 반환