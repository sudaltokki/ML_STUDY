# -*- coding: utf-8 -*-
#6. 시계열(timeseries) 데이터
#시계열 데이터를 데이터프레임의 행 인덱스로 사용하면, 시간으로 기록된 데이터를 분석하는 것이 매우 편리
#시계열 데이터 표현 방식: Timestamp(특정한 시점 기록), Period(두 시점 사이의 일정한 기간 나타냄)


#6-1) 다른 자료형을 시계열 객체로 변환
# 접하게 되는 문자열 또는 숫자로 저장되는 시간 데이터를, 판다스 시계열 객체인 Timestamp로 변환


#5-15. 문자열을 Timestamp로 변환 : pd.tp_datetime()
#다른 자료형을 판다스 Timestamp를 나타내는 datetime64로 변환
#line 27

# 라이브러리 불러오기
import pandas as pd

# read_csv() 함수로 CSV 파일을 가져와서 df로 변환
df = pd.read_csv('stock-data.csv')

# 데이터 내용 및 자료형 자료형 확인
print(df.head())
print('\n')
print(df.info())

# 문자열 데이터(시리즈 객체)를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])   #df에 새로운 열로 추가
#pd.to_datetime(df['']) 인자로 특정 열 전달

# 데이터 내용 및 자료형 자료형 확인
print(df.head())
print('\n')
print(df.info()) #'new_Date' 열의 자료형이 datetime64
print('\n')
print(type(df['new_Date'][0])) #'new_Date' 열의 모든 개별 원소데이터: Timestamp 객체 
print(df['new_Date'][0])
#한 열인 시리즈의 0번째 원소만 의미?


# 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정. 기존 날짜 열은 삭제
df.set_index('new_Date', inplace=True) #'new_Date'열의 데이터를 df의 행 인덱스로 지정
# 시계열값을 행 인덱스로 지정 시, 판다스는 datetimeIndex로 저장-> 클래스를 지원하므로 시간 순서에 맞춰 인덱싱 또는 슬라이싱 하기 편히

df.drop('Date', axis=1, inplace=True) # df.drop: 기존 'Date' 열 삭제

# 데이터 내용 및 자료형 자료형 확인
print(df.head())
print('\n')
print(df.info())
