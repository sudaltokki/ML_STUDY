# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx', engine='openpyxl')  # 데이터프레임 변환 

df_ns = df.iloc[[0, 5], 3:]            # 0~5행에 대해, 각각 3~끝 열까지 선택(남한, 북한 발전량 합계 데이터만 추출)
df_ns.index = ['South','North']        # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경!
print(df_ns.head())
print('\n')

# plot()의 디폴트: 선 그래프
df_ns.plot()

# x,y축 바꾸고 싶을 때: 행, 열 전치하여 다시 그리기
tdf_ns = df_ns.T #df.transpose()
print(tdf_ns.head())
print('\n')
tdf_ns.plot()