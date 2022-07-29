# -*- coding: utf-8 -*-
#1-3. 데이터프레임 객체에 함수 매핑 : df.pipe(매핑 함수)
# 반환하는 객체 종류: 매핑함수의 리턴값에 따라 결정(df/series/개별 값)


# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]

# 각 열의 NaN 찾기 - 데이터프레임 전달하면 데이터프레임을 반환
def missing_value(x):    
    return x.isnull()    

# 각 열의 NaN 개수 반환 - 데이터프레임 전달하면 각 열의 누락 데이터 개수를 시리즈 반환
def missing_count(x):    # 
    return missing_value(x).sum()
# line 14 에서 정의된 함수 이용, df반환 후
#sum() 실행 시 df의 각 열에 대해 누락 데이터 개수 반환(누락데이터이면 1(True)이므로, sum 이용 시 개수)
#df. sum() : default 열 기준,각 열에 대해 합계 값을 series로 반환
# https://www.delftstack.com/ko/api/python-pandas/pandas-dataframe-dataframe.sum-function/

# 데이터프레임의 총 NaN 개수 - 데이터프레임 전달하면 값을 반환
def totoal_number_missing(x):    
    return missing_count(x).sum()
#line 18에서 정의된 함수 이용하여 원본 df의 각 열의 합계에 대한 series를 구하고
#해당 series의 총 합계를 구함-> 원본df의 총 누락 데이터 개수 반환, 하나의 데이터 반환
    
# 데이터프레임에 pipe() 메소드로 함수 매핑
result_df = df.pipe(missing_value)   
print(result_df.head())
print(type(result_df))
print('\n')

result_series = df.pipe(missing_count)   
print(result_series)
print(type(result_series))
print('\n')

result_value = df.pipe(totoal_number_missing)   
print(result_value)
print(type(result_value))