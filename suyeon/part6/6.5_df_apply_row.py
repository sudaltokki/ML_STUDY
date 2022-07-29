# -*- coding: utf-8 -*-
#데이터프레임의 각 행에 함수 매핑: df.apply(매핑함수, axis=1)
#함수 결과가 0행부터 각 행에 입력됨 (모든 행의 연산 결과를 한데 모아 시리즈 객체 반환)
#??

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())
print('\n')

# 사용자 함수 정의
def add_two_obj(a, b):    # 두 객체의 합
    return a + b
    
# 데이터프레임의 2개 열을 선택하여 적용
# x=df, a=df['age'], b=df['ten']
df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)  
#??

#좌변 실행 결과를 df에 'add'열에 추가 
print(df.head())
