# -*- coding: utf-8 -*-
#2. 중복 데이터 처리
#5-6. 중복 데이터 확인: df.duplicated()
#해당 행이 이전에 나온 행과 중복시 True, 처음 나오는 행이면 False



# 라이브러리 불러오기
import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
print(df)
print('\n')

# 데이터프레임 전체 행 데이터 중에서 중복값 찾기
df_dup = df.duplicated()
print(df_dup)
print('\n')
#0행 데이터는 1행 데이터와 동일하지만, 0행 이전에 중복되는 행이 없으므로 False
#즉 중복 행들 중 제일 먼저 나오는 행만 중복이 아닌 행으로 처리


# 데이터프레임의 특정 열 데이터(시리즈)에서 중복값 찾기
col_dup = df['c2'].duplicated()
print(col_dup)