# -*- coding: utf-8 -*-
#1-7. 박스 플롯: .boxplot(x=a,b,c, labels=[])
#범주형 데이터 분포 파악 : 최소, 1분위, 중간, 3분위, 최대 의 5개 지표 제공



# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "./malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use('seaborn-poster')            # 스타일 서식 지정
plt.rcParams['axes.unicode_minus']=False   # 마이너스 부호 출력 설정

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 2, 1) #그림틀을 2개의 axe객체로 분할하기 위함(1개로 분할하는 경우에는 필요 없는 부분)
ax2 = fig.add_subplot(1, 2, 2)

# axe 객체에 boxplot 메서드로 그래프 출력
ax1.boxplot(x=[df[df['origin']==1]['mpg'], #boxplot으로 나타내고 싶은 3개 행의 mpg값을 선택하여 리스트!로 전달
               df[df['origin']==2]['mpg'], #행은 origin값에 따라 구분(이전 예제에서 그룹화 하는 것과 결과적으로 동일)
               df[df['origin']==3]['mpg']], 
         labels=['USA', 'EU', 'JAPAN']) #각 x축 눈금 라벨 추가

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
         labels=['USA', 'EU', 'JAPAN'],
         vert=False) #vert=False: 수평 박스 플롯 (vert: default True, 수직 박스 플롯)

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

plt.show()