# -*- coding: utf-8 -*-
#4-3. 데이터프레임 결합
#판다스 join()메소드는  merge함수를 기반이나, 두 df의 행 인덱스를 기준으로 결합하는 차이
#on=keys 설정 시, 행 인덱스 대신 다른 열 기준 결합 가능

#행 인덱스 기준 결합: df1.join(df2, how='left')

# 라이브러리 불러오기
import pandas as pd

# IPyhton 디스플레이 설정 변경 
pd.set_option('display.max_columns', 10)                  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)                 # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('./stock price.xlsx', index_col='id', engine= 'openpyxl')
df2 = pd.read_excel('./stock valuation.xlsx', index_col='id', engine= 'openpyxl')
#index_col='id': id 열을 두 생성 df의 행 인덱스로 설정


# 데이터프레임 결합(join)
df3 = df1.join(df2) 
# default: 왼쪽의 df1의 행 인덱스 기준으로 결합(how='left')
print(df3)
print('\n')

# 데이터프레임 결합(join) - 교집합: df1.join(df2, how='inner')
df4 = df1.join(df2, how='inner')
#두 df에 공통으로 존재하는 행 인덱스(line 17에서 설정, id 열) 기준 추출
print(df4)

