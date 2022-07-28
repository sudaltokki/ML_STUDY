# -*- coding: utf-8 -*-

import pandas as pd

# 파일 경로를 찾고, 변수 file_path에 저장
file_path = './read_csv_sample.csv' # ./로 시작하면 현재 폴더에서 파일을 가져온다 (../는 이전 폴더로 이동)

# read_csv() 함수로 csv 파일을 데이터프레임으로 변환, 변수 df1에 저장
df1 = pd.read_csv(file_path)
print(df1)
print('\n')

# header 옵션으로 데이터프레임의 열이름으로 사용할 행 지정
# header = None 옵션
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

# index_col 옵션으로 데이터프레임의 행 인덱스가 되는 열을 지정
# index_col = None 옵션
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

# index_col = 'c0' 옵션
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
print('\n')

'''
CSV 파일이란? 데이터 값을 쉼표(,)로 구분하고 있다는 의미로 comma-separated values를 의미한다
쉼표(,)로 열을 구분하고 줄바꿈으로 행을 구분한다

header 옵션이 없으면 CSV 파일의 첫 행의 데이터가 열 이름이 된다.
index_col 옵션이 없으면 정수 0, 1, 2, ...가 행 인덱스로 설정된다.

CSV 파일에 따라 쉼표 대신 탭(\t)이나 공백(" ")으로 텍스트를 구분하기도 한다. 
이때는 구분자(sep 또는 delimiter) 옵션을 알맞게 입력해야 한다.

그 외 옵션들
names : 열 이름으로 사용할 문자열의 리스트
skiprows : skip하고 싶은 행을 결정
parse_dates : 날짜 텍스트를 datetime64로 변환할 것인지 설정
skip_footer : 마지막 몇 줄을 skip할 것인지 설정
encoding : 텍스트 인코딩 종류를 지
'''