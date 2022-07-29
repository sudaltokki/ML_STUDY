# -*- coding: utf-8 -*-
#6-18. 그룹 객체에 함수 매핑: 범용 메소드: group.apply(매핑 함수)
# apply(): 판다스 객체의 개별 원소를 특정 함수에 일대일로 매핑


# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 분할
grouped = df.groupby(['class']) 

# -집계 : 각 그룹별 요약 통계정보를 집계: x.describe()
agg_grouped = grouped.apply(lambda x: x.describe())   
print(agg_grouped)
print('\n')

# -z-score를 계산하는 사용자 함수 정의
def z_score(x):                          
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.apply(z_score)   #기본값 axis=0 
print(age_zscore.head())
print('\n')

# -필터링 : age 열의 데이터 평균이 30보다 작은 그룹만을 필터링하여 출력
age_filter = grouped.apply(lambda x: x.age.mean() < 30)  
# age 열의 데이터 평균이 30보다 작은 그룹만을 필터링
# 각 그룹 별로 불린 값 지정
print(age_filter)   
print('\n')
for x in age_filter.index:
    if age_filter[x]==True: #불린 값이 True인 그룹이면
        age_filter_df = grouped.get_group(x) #group.get_group(): ??해당 그룹 x자체를 추출하여 새 df에 저장
        # line37에서 True인 한 그룹의 모든 원소가 age_filter_df에 추가됨
        # age_filter_df는 계속 새롭게 생성되는 변수인것?? 
        # 아니면 계속 유지되는 df인데 우연히 예제에서 세번째 for에서 추가된 그룹 정보 행 인덱스가 다 작은것?
        print(age_filter_df.head()) 
        print('\n')
        
        
# https://yganalyst.github.io/data_handling/Pd_13/
# https://jimmy-ai.tistory.com/23
        