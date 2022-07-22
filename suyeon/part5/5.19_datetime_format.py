# -*- coding: utf-8 -*-
#6-3. 시계열 데이터 활용
#5-19. 날짜 데이터 분리
#연-월-일 날짜 데이터에서 일부를 분리하여 추출 가능


# 라이브러리 불러오기
import pandas as pd

# read_csv() 함수로 파일 읽어와서 df로 변환
df = pd.read_csv('stock-data.csv')

# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])   #df에 새로운 열로 추가
print(df.head())
print('\n')

# dt 속성을 이용하여 new_Date 열의 년월일 정보를 년, 월, 일로 구분
df['Year'] = df['new_Date'].dt.year  #각각 기존 df의 새로운 열로 추가
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())
print('\n')
#df.dt.year : 연도 추출, df.dt.month : 월 추출, df.dt.day : 일 추출 


# Timestamp를 Period로 변환하여 년월일 표기 변경하기 
df['Date_yr'] = df['new_Date'].dt.to_period(freq='A') #연도 나타내는 값 저장
df['Date_m'] = df['new_Date'].dt.to_period(freq='M') #연-월 나타내는 값 저장
#?? freq설정에 따라 결정되는 것?
print(df.head())
print('\n')

# 원하는 열을 새로운 행 인덱스로 지정
df.set_index('Date_m', inplace=True)
print(df.head())
