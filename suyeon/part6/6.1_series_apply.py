# -*- coding: utf-8 -*-
#<6. 데이터프레임의 다양한 응용>

#1. 함수 매핑
#1-1. 개별 원소에 함수 매핑
#6-1. 시리즈 원소에 함수 매핑

#함수 매핑: 시리즈 또는 데이터프레임의 개별 원소를 특정 함수에 일대일 대응시키는 과정
#사용자가 직접 만든 함수(lambda함수 포함) 적용 가능하므로 판다스 기본함수로 처리하기 어려운 복잡 연산을 적용하게 할 수 있음

#시리즈 원소에 함수 매핑: series객체.apply(매핑함수)
# 시리즈 원소의 개수만큼 리턴값을 맏아서 같은 크기의 시리즈 객체로 반환


# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())
print('\n')

# 사용자 함수 정의
def add_10(n):   # 10을 더하는 함수
    return n + 10

def add_two_obj(a, b):    # 두 객체의 합
    return a + b

print(add_10(10))
print(add_two_obj(10, 10))
print('\n')

# 시리즈 객체에 적용
sr1 = df['age'].apply(add_10)               # n = df['age']의 모든 원소
print(sr1.head())
print('\n')
  
# 시리즈 객체와 숫자에 적용 : 2개의 인수(시리즈 + 숫자)
sr2 = df['age'].apply(add_two_obj, b=10)    # a=df['age']의 모든 원소, b=10
print(sr2.head())
print('\n')

# 람다 함수 활용: 시리즈 객체에 적용
sr3 = df['age'].apply(lambda x: add_10(x))  # x=df['age']
print(sr3.head())

#lambda 함수: def 이용하지 않고(함수 이름 없이) 함수 사용 가능
#https://digital-play.tistory.com/56

