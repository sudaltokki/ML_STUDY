# -*- coding: utf-8 -*-

import pandas as pd

dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9],
             'c3':[10, 11, 12], 'c4':[13, 14, 15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# sort_values() 메소드를 사용하여 특정 열의 데이터를 기준으로 데이터프레임 정렬

# c1 열을 기준으로 내림차순 정렬
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)
