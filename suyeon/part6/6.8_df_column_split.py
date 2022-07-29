# -*- coding: utf-8 -*-
#2-2. 열 분리
# 하나의 열이 여러가지 정보 담고 있을 때 각 정보를 분리해서 사용하는 경우('연월일','성이름')

# 라이브러리 불러오기
import pandas as pd

# 데이터셋 가져오기(엑셀을 데이터프레임으로 변환)
df = pd.read_excel('./주가데이터.xlsx', engine= 'openpyxl')
print(df.head(), '\n')
print(df.dtypes, '\n')

# 연, 월, 일 데이터 분리하기
df['연월일'] = df['연월일'].astype('str')   # 문자열 메소드 사용을 자료형 변경
#astype(): 자료형  변경

dates = df['연월일'].str.split('-')        # 문자열을 split() 메서드로 분리( [연,월,일] 형태의 리스트로 정리됨)
#시리즈의 str 속성으로 문자열 데이터에 접근
#반환되는 객체: series
# str.split('') :인자 기준으로 나눔, 문자열을 리스트로 변환 
#https://bio-info.tistory.com/29
print(dates.head(), '\n')


# 분리된 정보를 각각 새로운 열에 담아서 df에 추가하기
#원소인 문자열 리스트의 원소 선택: get
#각 원소 리스트의 인덱스 0,1,2를 전달하여 연, 월,일 데이터를 따로 선택

#시리즈의 원소 문자열 리스트 인덱싱: series.str.get(인덱스)

df['연'] = dates.str.get(0)     # dates 변수의 원소 리스트의 0번째 인덱스 값
# 선택된 인덱스의 값을 df의 '연'열을 생성하여 저장
df['월'] = dates.str.get(1)     # dates 변수의 원소 리스트의 1번째 인덱스 값 
df['일'] = dates.str.get(2)     # dates 변수의 원소 리스트의 2번째 인덱스 값
print(df.head())