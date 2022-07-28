# -*- coding: utf-8 -*-

import pandas as pd

dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9],
             'c3':[10, 11, 12], 'c4':[13, 14, 15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 행 인덱스를 기준으로 데이터프레임을 오름차순 또는 내림차순으로 정렬

# 내림차순으로 행 인덱스 정렬
ndf = df.sort_index(ascending=False)
print(ndf)
print('\n')

# 내림차순으로 행 인덱스 정렬
ndf2 = ndf.sort_index(ascending=True)
print(ndf2)
