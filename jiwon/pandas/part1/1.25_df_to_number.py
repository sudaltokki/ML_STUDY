# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns

'''
Seaborn 라이브러리에서 제공하는 데이터셋 중에서 타이타닉 데이터셋을 사용
타이타닉호 탑승자에 대한 인적사항과 구조 여부 등을 정리한 자료 (뭔가 귀엽다)
load_dataset() 함수로 불러온다
''' 

# titanic 데이터셋에서 fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head()) # 상위 다섯 개 행을 출력하는 함수
print('\n')
print(type(df))
print('\n')

# 데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.head())
print('\n')
print(type(addition))


# 데이터프레임에 숫자 10을 더하면 모든 원소에 숫자 10을 더해진 동일한 형태의 새로운 데이터프레임을 반환한다.
