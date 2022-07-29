# -*- coding: utf-8 -*-
#3. 필터링: series 또는 dataframe의 데이터 중 특정 조건식을 만족하는 원소만 따로 추출
#가장 대표적 필터링 방법: 불린 인덱싱(boolean indexing)

#3-1. 불린 인덱싱 : df[불린 시리즈]
#시리즈 객체에 어떤 조건식을 적용하면, 각 원소에 대해 참거짓을 판별하여 불린 값으로 구성된 시리즈 반환
#참에 해당하는 데이터 값을 따로 선택도 가능
#df의 각 열이 시리즈 객체이므로, 조건식 적용 시 각 원소에 대해 연산하여 불린 시리즈 반환 가능
#해당 불린 시리즈를 df에 대입 시 조건 만족 행만 선택 가능


# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 로딩
titanic = sns.load_dataset('titanic')

# 나이가 10대(10~19세)인 승객만 따로 선택하여 mask1에 시리즈 객체 저장(해당 열의 각 원소(레코드)의 참 거짓)
mask1 = (titanic.age >= 10) & (titanic.age < 20) #& AND연산자: 두 조건 모두 참인 경우에만 추출
df_teenage = titanic.loc[mask1, :]
# df.loc[불린 시리즈, :]: df의 행 인덱스 위치에 불린 시리즈 대입 시 
# 해당 조건 만족하는 행(레코드) 만 남게 됨 (해당 열도 불린이 기존 데이터값이 남는지 아닌지로 결정하여 해당 데이터값이 남게 됨)
# (모든 열 선택: 각 레코드의 모든 속성(나이, 성별 '''))

print(df_teenage.head())
print('\n')

#서로 다른 두 열에도 각각 다른 조건식 적용 가능
# 나이가 10세 미만(0~9세)이고 여성인 승객만 따로 선택
mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :]
print(df_female_under10.head())
print('\n')

# 나이가 10세 미만(0~9세) 또는 60세 이상인 승객의 age, sex, alone 열만 선택
mask3 = (titanic.age < 10) | (titanic.age >= 60) #| OR 연산자 이용(shift \)
df_under10_morethan60 = titanic.loc[mask3, ['age', 'sex', 'alone']] #추출하려는 열이름 지정
print(df_under10_morethan60.head())