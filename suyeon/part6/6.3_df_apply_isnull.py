# -*- coding: utf-8 -*-
#1-2. 시리즈 객체에 함수 매핑
#데이터프레임의 각 열에 함수 매핑: df.apply(매핑함수, axis=0)
#매칭 함수에 따라 반환되는 객체의 종류가 달라짐
#시리즈를 입력받고 시리즈를 반환하는 함수 매핑 시 df반환
#데이터프레임의 열을 매핑 함수에 전달하면 각 열의 리턴 값은 시리즈 형태로 반환
# 이들 시리즈가 하나의 데이터프레임으로 통합되는 과정 거침


# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')

# 사용자 함수 정의
def missing_value(series):    # 시리즈를 인수로 전달
    return series.isnull()    # 불린 시리즈를 반환
#isnull:isnull() 메소드는 (df의 각 원소)관측치가 결측이면 True, 결측이 아니면 False의 boollean 값을 반환
#https://rfriend.tistory.com/260

    
# 데이터프레임의 각 열을 인수로 전달하면 데이터프레임을 반환
result = df.apply(missing_value, axis=0)  
print(result.head())
print('\n')
print(type(result))