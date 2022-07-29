# -*- coding: utf-8 -*-
#7. 피벗
#피벗테이블을 구성하는 4가지 요소(행 인덱스, 열 인덱스, 데이터 값, 데이터 집계 함수)에 적용
#데이터프레임의 열을 각각 지정하여 함수(pd.pivot_table())의 인자로 전달


# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# IPyhton 디스플레이 설정 변경 
pd.set_option('display.max_columns', 10)    # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)    # 출력할 열의 너비

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]
print(df.head())
print('\n')


#- 행, 열, 값, 집계에 사용할 열을 1개씩 지정 - 평균 집계
pdf1 = pd.pivot_table(df,              # 피벗할 데이터프레임
                     index='class',    # 행 위치에 들어갈 열
                     columns='sex',    # 열 위치에 들어갈 열
                     values='age',     # 데이터로 사용할 열
                     aggfunc='mean')   # 데이터 집계 함수

print(pdf1.head())
print('\n')

# -값에 적용하는 집계 함수를 2개 이상 지정 가능 - 생존율, 생존자 수 집계
pdf2 = pd.pivot_table(df,                       # 피벗할 데이터프레임
                     index='class',             # 행 위치에 들어갈 열
                     columns='sex',             # 열 위치에 들어갈 열
                     values='survived',         # 데이터로 사용할 열
                     aggfunc=['mean', 'sum'])   # 데이터 집계 함수

print(pdf2.head())
print('\n')
# 행 인덱스: class열의 3가지 값
# 열 인덱스: 2중 멀티 인덱스: 데이터 집계 함수인 mean, sum이 높은 층,
    # 'sex'열 값인 female, male이 다음 층 구성
# survived의 mean: 생존율, sum: 생존자수


# -행, 열, 값에 사용할 열을 2개 이상 지정 가능 - 평균 나이, 최대 요금 집계
pdf3 = pd.pivot_table(df,                       # 피벗할 데이터프레임
                     index=['class', 'sex'],    # 행 위치에 들어갈 열
                     columns='survived',        # 열 위치에 들어갈 열
                     values=['age', 'fare'],    # 데이터로 사용할 열
                     aggfunc=['mean', 'max'])   # 데이터 집계 함수
# 행: 2중 구조
# 열: 3중 구조(데이터 집계 함수(mean, max) > 데이터값 구분(age, fare)> column 구분)

# IPython Console 디스플레이 옵션 설정
pd.set_option('display.max_columns', 10)        # 출력할 열의 개수 한도
print(pdf3.head())
print('\n')

# 행, 열 구조 살펴보기: .index, .comlumns; multiindex클래스 객체
print(pdf3.index)
print(pdf3.columns)
print('\n')
# multiindex 속성:levels=[[],[]] : 각 인덱스 별 데이터 값
#   labels=[]??????
#   names=[,]: 각 인덱스 종류 이름(aggfunc 제외)



# xs 인덱서 사용 - 행 선택(default: axis=0)
# .xs(): default: 행 인덱스에 접근, 축 axis=0 자동 설정 
#하나의 행 인덱스
print(pdf3.xs('First'))              # 행 인덱스가 First인 행을 선택 
print('\n')

#두개의 행 인덱스
print(pdf3.xs(('First', 'female')))   # 행 인덱스가 ('First', 'female')인 행을 선택
# 두 인덱스를 투플(,)로 전달
#행인덱스 level0, 행인덱스 level1의 값을 각각 선택 가능
print('\n')

#행 인덱스 레벨 직접 지정
#하나의 인덱스 지정
print(pdf3.xs('male', level='sex'))  # 행 인덱스의 sex 레벨이 male인 행을 선택
print('\n')
#두개의 인덱스 지정
print(pdf3.xs(('Second', 'male'), level=[0, 'sex']))  # Second, male인 행을 선택
print('\n')
# 인덱스 값은 투플로 전달, level은 리스트[,]로 전달


# xs 인덱서 사용 - 열 선택(axis=1 설정)
#하나의 열 인덱스 지정
print(pdf3.xs('mean', axis=1))        # 열 인덱스가 mean인 데이터를 선택 
print('\n')

#두 개의 열 인덱스 지정
print(pdf3.xs(('mean', 'age'), axis=1))   # 열 인덱스가 ('mean', 'age')인 데이터 선택
print('\n')

#열 인덱스 레벨 직접 지정
print(pdf3.xs(1, level='survived', axis=1))  # survived 레벨이 1인 데이터 선택
print('\n')
#여기서 1: pdf3에서 인덱스로서 survived 여부를 나타냄

#여러개의 열 인덱스 레벨 직접 지정(인덱스값은 투플로, 레벨은 리스트로)
print(pdf3.xs(('max', 'fare', 0), 
              level=[0, 1, 2], axis=1))  # max, fare, survived=0인 데이터 선택
#열인덱스 level0: mean, max 중 max
#   level1: fare, age 중 fare
#   level2: 0, 1(survived) 중 0
# 열 인덱스 3중구조 line 54에서 확인