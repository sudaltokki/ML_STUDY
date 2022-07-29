# -*- coding: utf-8 -*-
#6. 멀티 인덱스
#groupby메소드에 여러개의 열을 리스트로 전달 시, 각 열로 다중 행 인덱스 구성되는 경우: 멀티 인덱스 클래스



# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열, sex 열을 기준으로 분할
grouped = df.groupby(['class', 'sex'])  

# 그룹 객체에 연산 메서드 적용
gdf = grouped.mean()
print(gdf)
print('\n')
print(type(gdf)) #dataframe

#- 멀티인덱스에서 하나의 인덱스만 사용하는 경우: .loc[]
# class 값이 First인 행을 선택하여 출력
print(gdf.loc['First'])
print('\n')

#-멀티인덱스에서 두개의 인덱스 사용하는 경우 : loc[(,)]
#    인자로는 투플 형태(,) 각 인덱스에서 찾는 값 전달
# class 값이 First이고, sex 값이 female인 행을 선택하여 출력
print(gdf.loc[('First', 'female')])
print('\n')

#-멀티인덱스에서 하나의 인덱스 사용하는 경우: .xs(찾는 인덱스 값, level= 인덱스 종류)
# sex 값이 male인 행을 선택하여 출력
print(gdf.xs('male', level='sex'))
print('\n')

#https://seong6496.tistory.com/157
#.xs를 멀티인덱스에서 주로 사용
# print(gdf.loc['female']) 이 경우 오류 발생하기 때문
#.loc[]: 하나의 인덱스만 사용하는 경우, 멀티인덱스 중 더 큰 범주에 대해서만 가능하므로
# .xs(): level선택하여 멀티인덱스 중 더 큰/작은 범주 자유롭게 지정 가능