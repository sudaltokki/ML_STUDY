# -*- coding: utf-8 -*-
"""
p53, 1-25
"""

import pandas as pd
import seaborn as sns
"""seaborn라이브러리는 다양한 내장 데이터셋을 제공, 필요한 데이터셋 바로 사용 가능"""

titanic = sns.load_dataset('titanic')
df=titanic.loc[ : , ['age','fare']]

print(df.head())
print('\n')
print(type(df))
print('\n')


addition= df+10
print(addition.head())
print('\n')
print(type(addition))
print('\n')