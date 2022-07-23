# -*- coding: utf-8 -*-

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

# 각 열(연도)에서 전출지는 서울시이고, 전입지는 서울시가 아닌 데이터만 추출(서울에서 다른 지역으로 이동한 데이터만 추출하여 정리)
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask] #새 df 생성
df_seoul = df_seoul.drop(['전출지별'], axis=1) #'전출지별' 열 삭제(모두 서울시로 동일하므로)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)#'전입지별' 열 이름 변경, 기존 df 변경
df_seoul.set_index('전입지', inplace=True) #행 인덱스 설정

# '경기도'열 선택하여 따로 추출(서울에서 경기도로 이동한 인구 데이터 값만 선택)
sr_one = df_seoul.loc['경기도']

# 스타일 서식 지정 (print(plt.style.available) 로 가능한 모든 스타일 리스트 출력 가능)
plt.style.use('ggplot') #matplotlib 설정지정-> 다른 실행 파일에서도 적용. 초기화하려면 스파이더 자체를 다시 실행

# 그림 사이즈 지정
plt.figure(figsize=(14, 5))

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation='vertical') #rotation=90 (반시계방향 90도 회전과 동일)

# x, y축 데이터를 plot 함수에 입력 
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)  # 마커 표시 추가(원 모양의 점, 마커 사이즈 설정)
#plt.plot(sr_one) (x,y축 변경 필요 없는 경우이므로 동일)

plt.title('서울 -> 경기 인구 이동', size=30)  #차트 제목
plt.xlabel('기간', size=20)                  #x축 이름
plt.ylabel('이동 인구수', size=20)           #y축 이름

plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)   #범례 표시

plt.show()  # 변경사항 저장하고 그래프 출력
