# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 누락 데이터(NaN)를 0으로 채움
df = pd.read_excel('시도별 전출입 인구수.xlsx',header=0).fillna(0)
print(df.head())

# method='ffill' 옵션을 사용하면 누락 데이터가 들어 있는 행의 바로 앞에 위치한 행의 데이터 값으로 채운다
df2 = pd.read_excel('시도별 전출입 인구수.xlsx',header=0).fillna(method='ffill')
print(df2.head())

# 전출지가 서울특별시이고 전입지가 서울특별시가 아닌 데이터만 추출
mask = (df2['전출지별'] == '서울특별시') & (df2['전입지별'] != '서울특별시')
df_seoul = df2[mask]

# '전출지별' 열 없애기(어차피 다 서울특별시)
df_seoul = df_seoul.drop(['전출지별'], axis=1) # '전출지별' 열 없애기(어차피 다 서울특별시)
# '전입지별'이라는 열의 이름을 '전입지'로 바꿈
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# '전입지' 열을 index로 설정
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)
print('\n')

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']
print(sr_one.head())


'''
화면 분할하여 그래프 여러 개 그리기
figure() 함수를 사용해 그래프를 그리는 그림틀(fig) 생성
figsize 옵션으로 그림틀 크기 결정
fig 객체에 add_subplot() 메소드를 적용하여 그림틀을 여러 개로 분할, 이 때 나눠진 각 부분을 axe 객체라고 부른다
add_subplot() 메소드 인자에 행의 크기, 열의 크기, 서브플롯 순서를 순서대로 입력
'''
# 그래프 객체 생성(figure에 2개의 서브 플롯 생성)
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# axe 객체에 plot 함수로 그래프 출력
ax1.plot(sr_one, 'o', markersize=10)
ax2.plot(sr_one, marker='o', markerfacecolor='green', markersize=10,
         color='olive', linewidth=2, label='서울 -> 경기')
ax2.legend(loc='best') # label 옵션과 legend() 메소드를 적용해 범례 표시


# y축 범위 지정(최소값, 최대값)
ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

# 축 눈금 라벨 지정 및 75도 회전
ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)

# 변경사항 저장하고 그래프 출력
plt.show()
