# -*- coding: utf-8 -*-

import pandas as pd

# 딕셔너리 정의
dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9],
             'c3':[10, 11, 12], 'c4':[13, 14, 15]}


# 딕셔너리를 데이터프레임으로 변환. 인덱스 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 인덱스 재지정
new_index = ['r4', 'r3', 'r2', 'r1', 'r0']
ndf = df.reindex(new_index)
print(ndf)
print('\n')

# reindex로 발생한 NaN값을 대체할 값 지정
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)

