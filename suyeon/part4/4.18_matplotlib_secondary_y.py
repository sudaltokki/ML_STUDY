# -*- coding: utf-8 -*-
# 4-18. 2축 그래프 그리기(보조 축 활용하기)
#line 25부터 확인


# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "./malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use('ggplot')   # 스타일 서식 지정
plt.rcParams['axes.unicode_minus']=False   # 마이너스 부호 출력 설정

# Excel 데이터를 데이터프레임 변환 
df = pd.read_excel('./남북한발전전력량.xlsx', engine= 'openpyxl', convert_float=True)
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True)
df = df.T 

# 증감율(변동률) 계산
df = df.rename(columns={'합계':'총발전량'}) #'합계' 열 이름을 '총발전량'으로 변환
df['총발전량 - 1년'] = df['총발전량'].shift(1) #.shift() : 행 이동 (https://cosmosproject.tistory.com/390)
#'총발전량' 열을 1행씩 뒤로 이동시킨 새로운 데이터를, '총발전량-1년' 열을 생성하여 저장함 

df['증감율'] = ((df['총발전량'] / df['총발전량 - 1년']) - 1) * 100      
#좌변의 계산 데이터를, '증감율' 열을 생성하여 저장

# 2축 그래프 그리기
ax1 = df[['수력','화력']].plot(kind='bar', figsize=(20, 10), width=0.7, stacked=True)  #stacked=True로 각 열별 수력, 화력 데이터를 쌓아서 표시 
ax2 = ax1.twinx() # .twinx() : 쌍둥이 객체 반환
ax2.plot(df.index, df.증감율, ls='--', marker='o', markersize=20, 
         color='green', label='전년대비 증감율(%)')  #ls='--': line style을 점선으로 설정

ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량(억 KWh)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30)
ax1.legend(loc='upper left')

plt.show()