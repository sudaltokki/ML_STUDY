# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail()) # 하위 다섯 개 행을 출력하는 함수
print('\n')
print(type(df))
print('\n')

addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))
print('\n')

# 데이터프레임끼리 연산하기
subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))


# 각 데이터프레임의 같은 행, 같은 열 위치에 있는 원소끼리 계산한다.
