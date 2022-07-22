# -*- coding: utf-8 -*-
#화면 분할하여 여러개 그리기
#line 34부터 참고


# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "./malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임 변환 
df = pd.read_excel('시도별 전출입 인구수.xlsx', engine= 'openpyxl', header=0)

# 전출지별에서 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# 스타일 서식 지정
plt.style.use('ggplot') 

#4-8
# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(10, 10)) #.figure() : 그래프 그릴 그림틀 생성
ax1 = fig.add_subplot(2, 1, 1)  #.add_subplot(): 인자: 행의 크기, 열의 크기, 서브플롯 순서  (서브플롯 개수 또는 axe 객체 개수=행*열)
ax2 = fig.add_subplot(2, 1, 2)

# axe 객체에 plot 함수로 그래프 출력
ax1.plot(sr_one, 'o', markersize=10) #선을 그리지 않고 점으로만 표시
ax2.plot(sr_one, marker='o', markerfacecolor='green', markersize=10, 
         color='olive', linewidth=2, label='서울 -> 경기')
ax2.legend(loc='best')  # legend(범례)의 위치 설정: 자동 계산된 최적 위치에 설정 (그 외 옵션과 legend 설정 : https://kongdols-room.tistory.com/87)

#y축 범위 지정 (최소값, 최대값)
ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

# 축 눈금 라벨 지정 및 75도 회전(반시계) : set_xticklabels()
ax1.set_xticklabels(sr_one.index, rotation=75)   #(예제 4-4) .xticks(rotation=''):  이미 존재하는 라벨에 대하여 회전만 설정
ax2.set_xticklabels(sr_one.index, rotation=75)


#4-9
# 차트 제목 추가
ax1.set_title('서울 -> 경기 인구 이동', size=20)

# 축이름 추가
ax1.set_xlabel('기간', size=12)
ax1.set_ylabel('이동 인구수', size = 12)

plt.show()  # 변경사항 저장하고 그래프 출력