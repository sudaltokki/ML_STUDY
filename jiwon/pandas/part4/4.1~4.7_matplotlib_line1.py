# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

'''
판다스는 데이터 시각화를 지원하는 내장 기능이 있지만, 풍부한 편이 아니다.
Matplotlib은 파이썬 표준 시각화 도구라고 부를 수 있을 정도로 2D 평면 그래프에 관한 다양한 포맷과 기능을 지원한다.
'''

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

# 스타일 서식 지정
# 'ggplot' 외에도 많은 종류의 스타일 서식 지원
plt.style.use('ggplot')

# 그림 사이즈 지정 (가로 14인치, 세로 5인치)
plt.figure(figsize=(14, 5))

# x축 눈금 라벨 회전
plt.xticks(rotation='vertical')


# x, y축 데이터를 plot 함수에 입력 (시리즈의 인덱스를 x축, 데이터 값을 y축 데이터로 전달)
# plt.plot(sr_one)와 같은 결과를 낸다 / 원 모양의 점을 마커로 표시, 마커 사이즈 10
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)

# 차트 제목 추가
plt.title('서울 -> 경기 인구 이동')

# 축 이름 추가
plt.xlabel('기간')
plt.ylabel('이동 인구수')

# 범례 표시
plt.legend(labels=['서울 -> 경기'], loc='best')

# 주석을 넣을 여백 공간을 확보하기 위해 y축 범위 지정(최소값, 최대값)
plt.ylim(50000, 800000)

# 주석 표시 - 화살표
# arrowprops 옵션을 사용하면 텍스트 대신 화살표가 표시
plt.annotate('', 
             xy=(20, 620000), # 화살표 끝점
             xytext=(2, 290000), # 화살표 시작점
             xycoords='data', # 좌표체계
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5), # 화살표 서식
             )

plt.annotate('', 
             xy=(47, 450000), # 화살표 끝점
             xytext=(30, 580000), # 화살표 시작점
             xycoords='data', # 좌표체계
             arrowprops=dict(arrowstyle='->', color='olive', lw=5), # 화살표 서식
             )

# 주석 표시 - 텍스트
# rotation 옵션에서 양의 회전 방향은 반시계방향
# va 옵션은 글자를 세로 방향으로 정렬, ha 옵션은 글자를 가로 방향으로 정렬
plt.annotate('인구 이동 증가(1970-1995)', # 텍스트 입력
             xy=(10, 360000), # 텍스트 위치 기준점
             rotation=25, # 텍스트 회전 각도
             va='baseline', # 텍스트 상하 정렬
             ha='center', # 텍스트 좌우 정렬
             fontsize=15, # 텍스트 크기
             )

plt.annotate('인구 이동 감소(1995-2017)', # 텍스트 입력
             xy=(40, 490000), # 텍스트 위치 기준점
             rotation=-10, # 텍스트 회전 각도
             va='baseline', # 텍스트 상하 정렬
             ha='center', # 텍스트 좌우 정렬
             fontsize=15, # 텍스트 크기
             )


# 변경사항 저장하고 그래프 출력
plt.show()