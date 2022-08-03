# -*- coding: utf-8 -*-

'''
판다스 내장 plot() 메소드로 그래프 그리기, kind 옵션으로 그래프 종류 선택

kind 옵션
'line' - 선 그래프 (default)
'bar' - 수직 막대 그래프
'barh' - 수평 막대 그래프
'hist' - 히스토그램
'box' - 박스 플롯
'kde' - 커널 밀도 그래프
'area' - 면적 그래프
'pie' - 파이 그래프
'scatter' - 산점도 그래프
'hexbin' - 고밀도 산점도 그래프
'''

import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:] # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South', 'North'] # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경
print(df_ns)
print('\n')

# 선 그래프 그리기
df_ns.plot()

# 시간의 흐름에 따른 연도별 발전량 변화 추이를 보기 위해서 연도 값을 x축에 표시하는 것이 적절하다
# 행, 열 전치하여 다시 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot()