# -*- coding: utf-8 -*-

#5-20. 날짜 인덱스 활용

#Timestamp열을 행 인덱스 지정 시 DatetimeIndex라는 고유 속성으로 변환
#Period ''   PeriodIndex

#날짜 인덱스:  시계열 데이터에 대한 인덱싱과 슬라이싱 편리


# 라이브러리 불러오기
import pandas as pd

# read_csv() 함수로 파일 읽어와서 df로 변환
df = pd.read_csv('stock-data.csv')

# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])   # 새로운 열에 추가
df.set_index('new_Date', inplace=True)        # 행 인덱스로 지정

print(df.head())
print('\n')
print(df.index) #인덱스 속성이 DatetimeIndex인것 확인 가능
print('\n')

# 날짜 인덱스를 이용하여 데이터 선택하기
#연-월-일 중 필요한 레벨을 선택적 슬라이싱 가능
df_y = df['2018'] #연도 기준 선택
print(df_y.head())
print('\n')

df_ym = df.loc['2018-07']    # loc 인덱서 활용!
print(df_ym)  #연-월 기준 선택
print('\n')

df_ym_cols = df.loc['2018-07', 'Start':'High']    # 열 범위 슬라이싱 추가
print(df_ym_cols)
print('\n')

df_ymd = df['2018-07-02'] #연-월-일 기준 선택
print(df_ymd)
print('\n')

df_ymd_range = df['2018-06-25':'2018-06-20']    # 날짜 범위로 지정! #행 인덱스라는 것은 내용으로 확인가능?
#25일 데이터부터 20일 데이터까지 나열
#20일 데이터까지 포함. 왜 끝값이 제외되지 않음??
print(df_ymd_range)  
print('\n')

#Timestamp 객체로 표시된 두 날짜 사이의 시간 간격 구하기 (방식 알아두기)
# 시간 간격 계산. 최근 180일 ~ 189일 사이의 값들만 선택하기
today = pd.to_datetime('2018-12-25')            # 기준일 생성
df['time_delta'] = today - df.index             # 날짜 차이 계산( 리스트로 생성하여 df의 새 열로 저장)
df.set_index('time_delta', inplace=True)        # 행 인덱스로 지정
df_180 = df['180 days':'189 days'] #180~189 까지 나열
print(df_180)

