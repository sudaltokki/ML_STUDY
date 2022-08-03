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

'''
동일한 axe 객체에 여러 개의 그래프 추가하기
동일한 객체에 plot() 메소드 여러번 적용
'''

# 서울에서 '충청남도', '경상북도', '강원도'로 이동한 인구 데이터 값만 선택
col_years = list(map(str, range(1970, 2018))) # 1970 ~ 2018 문자열 리스트
df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도'], col_years]

# 스타일 서식 지정
plt.style.use('ggplot')

# 그래프 객체 생성(figure에 1개의 서브 플롯 생성)
fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(1, 1, 1)

# axe 객체에 plot 함수로 그래프 출력
ax.plot(col_years, df_3.loc['충청남도'], marker='o', markerfacecolor='green', markersize=10,
         color='olive', linewidth=2, label='서울 -> 충남')
ax.plot(col_years, df_3.loc['경상북도'], marker='o', markerfacecolor='blue', markersize=10,
         color='skyblue', linewidth=2, label='서울 -> 경북')
ax.plot(col_years, df_3.loc['강원도'], marker='o', markerfacecolor='red', markersize=10,
         color='magenta', linewidth=2, label='서울 -> 강원')
ax.legend(loc='best') # label 옵션과 legend() 메소드를 적용해 범례 표시

# 차트 제목 추가
ax.set_title('서울 -> 충남, 경북, 강원 인구 이동', size=20)

# 축 이름 추가
ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size=12)

# 축 눈금 라벨 지정 및 75도 회전
ax.set_xticklabels(col_years, rotation=90)

# 축 눈금 라벨 크기
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

# 변경사항 저장하고 그래프 출력
plt.show()
