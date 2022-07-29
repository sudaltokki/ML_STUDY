# -*- coding: utf-8 -*-
# 5-2. 그룹 연산 메소드(적용-결합 단계)

# 6-15. 데이터 집계: 그룹 객체에 대해서 다양한 연산 적용
# 데이터 집계 판다스 기본 함수: mean, max, min, sum, count, size, var, std, describe, info, first, last
# - 표준편차 데이터 집계(내장함수):group객체.std()
    #각 그룹(키값, 그룹 이름)을 행 인덱스로 갖는 df로 반환


# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 분할
grouped = df.groupby(['class']) 

# 각 그룹에 대한 모든 열의 표준편차를 집계하여 데이터프레임으로 반환
std_all = grouped.std()  
print(std_all)
print('\n')
print(type(std_all)) #df
print('\n')


# 각 그룹에 대한 fare 열의 표준편차를 집계하여 시리즈로 반환 
# 그룹 객체의 특정 열만의 표준편차 집계
#하나의 열 선택하므로 series로 반환
std_fare = grouped.fare.std()  
print(std_fare)
print('\n')
print(type(std_fare))
print('\n')




# -그룹 객체에 agg() 메소드 적용 - 사용자 정의 함수를 인수로 전달
# agg메소드 데이터 집계: group객체.agg(매핑 함수)
def min_max(x):    # 최대값 - 최소값 : 데이터 값의 분포 범위 알 수 있음(위의 표준편차 구하는 것과 비슷한 해석 가능)
    return x.max() - x.min()
    # 
    
# 각 그룹의 최대값과 최소값의 차이를 계산하여 그룹별로 집계
agg_minmax = grouped.agg(min_max)  
print(agg_minmax.head())
print('\n')


# 동시에 여러개의 함수 사용, 각 그룹별 데이터에 대한 집계
#   각각 열에 여러 함수를 일괄 매핑: group. agg([함수1, 함수2, ''']) 리스트 인수
#   각 열마다 다른 종류의 함수를 매핑: group. arr({'열1':함수1, '열2':함수2, '''}) 딕셔너리 인수

# 여러 함수를 각 열에 동일하게 적용하여 집계
agg_all = grouped.agg(['min', 'max'])  
print(agg_all.head())
print('\n')


# 각 열마다 다른 함수를 적용하여 집계
# 하나의 열에 여러 개 함수 적용 시 value에 리스트[]로 전달
    #2개의 연산 결과를 각각 집계하여 다른 열로 구분하여 표시
    #함수 명을 열이름에 추가하여 2중 열 구조
agg_sep = grouped.agg({'fare':['min', 'max'], 'age':'mean'})  
print(agg_sep.head())
