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
막대 그래프 : 데이터 값의 크기에 비례하여 높이를 갖는 직사각형 막대로 표현
세로형 막대 그래프는 시계열 데이터, 즉 시간적으로 차이가 나는 데이터들을 표현하는데 적합
plot() 메소드에 kind='bar' 옵션 입력
'''

# 서울에서 '충청남도', '경상북도', '강원도'로 이동한 인구 데이터 값만 선택
col_years = list(map(str, range(2010, 2018))) # 2010 ~ 2018 문자열 리스트
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
df_4 = df_4.transpose()

# 스타일 서식 지정
plt.style.use('ggplot')

# 데이터프레임의 인덱스를 정수형으로 변경(x축 눈금 라벨 표시)
df_4.index = df_4.index.map(int)

# 면적 그래프 axe 객체 생성
df_4.plot(kind='bar', figsize=(20, 10), width=0.7,
               color=['orange', 'green', 'skyblue', 'blue'])

plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간', size=20)
plt.ylim(5000, 30000)
plt.legend(loc='best', fontsize=15)

# 변경사항 저장하고 그래프 출력
plt.show()