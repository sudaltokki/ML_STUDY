# -*- coding: utf-8 -*-

#df열에 함수 매핑(apply)
# 시리즈를 입력받아서 하나의 값을 반환하는 함수 매핑 시 시리즈 객체 반환
#df의 각 열을 매칭 함수에 전달 시 각 열의 리턴값이 하나의 값으로 반환
#이들 값이 하나의 시리즈로 통함됨(각 열의 이름이 새 시리즈의 인덱스, 리턴값이 새 데이터값)
#default: axis=0

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')

# 사용자 함수 정의
def min_max(x):    # 시리즈의 최대값 - 시리즈의 최소값
    return x.max() - x.min()
    
# 데이터프레임의 각 열을 인수로 전달하면 시리즈를 반환
result = df.apply(min_max)   #기본값 axis=0 
print(result)
print('\n')
print(type(result))