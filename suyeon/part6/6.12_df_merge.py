# -*- coding: utf-8 -*-
#4-2. 데이터프레임 병합
# merge: 어떤 기준에 의해 두 데이터 프레임을 병합 (앞의 concat: 이어붙임)
# key: 기준이 되는 열이나 인덱스, 반드시 df 양쪽에 모두 존재해야함

# 데이터프레임 병합: pd.merge(df_left, df_right, how='inner', on=None) : default
# on= None : 두 df에 공통으로 속하는 모든 열을 기준(키)으로 병합
# how='inner': 기준이 되는 열의 데이터가 양쪽 데이터프레임에 공통으로 존재하는 교집합일 경우에만 추출
# 기준 열에 대해 공통인 행만 반환(교집합인 행을 반환)
# how='outer' : 합집합이 되는 행 반환

# 라이브러리 불러오기
import pandas as pd

# IPyhton 디스플레이 설정 변경 
pd.set_option('display.max_columns', 10)                  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)                 # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('./stock price.xlsx', engine= 'openpyxl')
df2 = pd.read_excel('./stock valuation.xlsx', engine= 'openpyxl')

print(df1)
print('\n')
print(df2)
print('\n')

# 데이터프레임 합치기 - 교집합 (default)
merge_inner = pd.merge(df1, df2)
#on=None인 경우, 첫번째 열(id) ???을 기준으로 공통으로 존재하는 5개 종목이 병합되어 출력
#이 예제의 경우 id와 stockname이 연결적이므로 stockname열은 병합되어도 하나의 값만 존재
print(merge_inner)
print('\n')


# 데이터프레임 합치기 - 합집합
merge_outer = pd.merge(df1, df2, how='outer', on='id')
#on='id':두 df의 공통 열 중 id열을 키로 병합
#how='outer': 기준이 되는 id열의 데이터가 어느 한쪽에만 속하더라도 포함
#어느 한쪽이라도 데이터가 없으면 NaN으로 지정
print(merge_outer)
print('\n')


# 데이터프레임 합치기 - 왼쪽 데이터프레임 기준, 키 값 분리
merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
#how='left': 왼쪽 데이터프레임의 키 열에 속하는 데이터값을 기준으로 병합
#(즉 왼쪽 키 열의 모든 데이터값은 표시되고, 오른쪽 df은 대응하는 왼쪽 키 데이터가 존재하는 경우에만 추가됨)

#left_on과 right_on 옵션: 좌우 데이터프레임에 가각 다르게 키 지정
#이 경우 키 열이 아닌 열(ex)'id' )이 양쪽 df에 모두 존재 시 id_x, id_y로 구분되어 표기됨
print(merge_left)
print('\n')


# 데이터프레임 합치기 - 오른쪽 데이터프레임 기준, 키 값 분리
merge_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
#how='right': 오른쪽 데이터프레임의 키 열을 기준으로 추출
# 오른쪽 df2의 'name'열에 들어있는 종목 데이터 기준 병합
print(merge_right)
print('\n')


# 불린 인덱싱과 결합하여 원하는 데이터 찾기
price = df1[df1['price'] < 50000]
print(price.head())
print('\n')
value = pd.merge(price, df2)
#default: how='inner', on='None': 두 df에 공통으로 존재하는 열(id)를 기준으로, 
#양쪽에 공통 값을 가지는 데이터가 추출

print(value)
#df2에 valuation데이터 가진 회사는 '모두투어리츠' 한 종목 뿐임