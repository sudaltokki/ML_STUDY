# -*- coding: utf-8 -*-
#2. 열 재구성
#2-1. 열 순서 변경
#열 이름을 원하는 순서대로 정리해 리스트를 만들고, df에서 열을 다시 선택하는 방식

#df의 열 순서 변경: df[재구성한 열 이름 리스트]

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋의 부분을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']
#파이썬 리스트 슬라이싱과 달리
# df 슬라이싱 시 마지막 범위의 값 포함됨
print(df, '\n')

# 열 이름의 리스트 만들기
columns = list(df.columns.values)   #기존 열 이름
# df.columns.values: df의 열 이름 배열
# list() : 배열이 df열의 원래 순서 유지한 상태로 리스트 변환
print(columns, '\n')

# 열 이름을 알파벳 순으로 정렬하기
columns_sorted = sorted(columns)    #알파벳 순으로 정렬: sorted()
df_sorted = df[columns_sorted] 
# 기존 df에서, columns_sorted에 저장된 순서로! 특정 열들 선택하여!
# df_sorted라는 새 df로 저장
print(df_sorted, '\n')

# 열 이름을 기존 순서의 정반대 역순으로 정렬하기
columns_reversed = list(reversed(columns)) #line19의 열임(not line 25)
#reversed(): 기존 순서의 정반대로 정렬
#https://itholic.github.io/python-reverse-reversed/
df_reversed = df[columns_reversed]
print(df_reversed, '\n')

# 열 이름을 사용자가 정의한 임의의 순서로 재배치하기
columns_customed = ['pclass', 'sex', 'age', 'survived']  
df_customed = df[columns_customed]
print(df_customed)
