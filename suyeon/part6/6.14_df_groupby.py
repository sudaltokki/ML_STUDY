# -*- coding: utf-8 -*-
#5. 그룹 연산
# 그룹 연산: 복잡한 데이터를 특정 기준을 적용하여 몇개의 그룹으로 분할하여 처리함
# 데이터 집계, 변환, 필터링 시 효율
# 3단계 과정:
    #1 분할 split: 데이터를 특정 조건에 의해 분할, 판다스 groupby() 메소드 사용
    #2 적용 apply: 데이터를 집계, 변환, 필터링하는데 필요한 메소드 적용
    #3 결합 combine: 2단계의 처리 결과를 하나로 결합

#5-1. 그룹 객체 만들기(분할 단계)
#6-14. 1개 열을 기준으로 그룹화
#그룹 연산(분할): df.groupby(기준이 되는 열)
    #기준이 되는 열: 1개도 가능, 여러 열은 리스트로 입력 가능

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

print('승객 수:', len(df)) 
#len(df) 시 행 개수 반환( https://www.delftstack.com/ko/howto/python-pandas/how-to-get-the-row-count-of-a-pandas-dataframe/)
print(df.head())
print('\n')

# class 열을 기준으로 분할
grouped = df.groupby(['class']) 
print(grouped) #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000029EB8AA0D00>
print('\n')
#class열 기준 groupby: First, Second, third의 세가지 그룹으로 분할
#반환 객체: dataframe groupby 객체, 기준 열의 값을 기준(key)로 정렬한 형태??


# 그룹 객체를 iteration으로 출력: head() 메소드로 첫 5행만을 출력
for key, group in grouped:
    # 위 코드: iterator를 돌면서 다른 key를 만나면 새 그룹을 만드는 식으로 동작하기 때문에, 같은 키라도 분산되어있으면 한 그룹에 뭉쳐지지 않음
    #아래 내용: 키를 만나면 키와 해당하는 원소 개수 출력
    #https://hulk89.github.io/python/2016/11/25/groupby/
    print('* key :', key)
    print('* number :', len(group))    
    print(group.head())
    print('\n')
# 각 승객의 행 인덱스는 원본 df대로 유지


    
#그룹 매체에 연산 메소드 적용: grouped.mean()
# 각 그룹별 평균값이 반환
# 연산이 가능한 열에 대해서만 선택적으로 연산 수행( 문자열 데이터 가진 열 제외)
average = grouped.mean()
print(average)
print('\n')

# 개별 그룹 선택하기: grouped.get_group('키값 (이름)')
#특정 키값 가진 데이터만 따로 선택하여 추출 가능
group3 = grouped.get_group('Third')
print(group3.head())
print('\n')


#여러 열을 기준으로 그룹화: df.groupby(기준이 되는 열 리스트)
#여러 개의 기준값 사용하므로 반환되는 그룹 객체의 인덱스는 다중 구조

# class 열, sex 열을 기준으로 분할
grouped_two = df.groupby(['class', 'sex']) 
# 두 열이 갖는 원소값들로 만들 수 있는 모든 조합으로 키 생성(예) (first, female), (first, males)''')) 
# 키: (class, sex)형식의 투플로 지정 (예제에서 키 개수: 3*2=6가지)

# grouped_two 그룹 객체를 iteration으로 출력
for key, group in grouped_two:
    print('* key :', key)
    print('* number :', len(group))    
    print(group.head())
    print('\n')
    
# grouped_two 그룹 객체에 연산 메소드 적용: grouped_two.mean()
# grouped_two 의 각 그룹에 mean() 적용
# df로 반환
# 키가 되는 2개 열(class,sex)로부터 2중 멀티 인덱스 지정 (출력 형식 보면 이해 가능)
average_two = grouped_two.mean()
print(average_two)
print('\n')
print(type(average_two))

# 멀티인덱스 이용하여 grouped_two 그룹 객체에서 특정 그룹 선택하기: get_group()
# 인자는 투플로 ('','')
# df 반환
# 행 인덱스는 원본 df에서와 동일하게 유지됨
group3f = grouped_two.get_group(('Third','female'))
print(group3f.head())