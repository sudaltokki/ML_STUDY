# -*- coding: utf-8 -*-
#Seaborn library 이용
#4-25. 데이터셋 가져오기, 4-26.회귀선이 있는 산점도


# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기: .load_dataset('데이터셋 이름')
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정:.set_style('') (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
 
# 산점도: sns.regplot(): 서로 다른 2개의 연속 변수 사이 산점도를 그리고 선형회귀분석에 의한 회귀선 함께 표시
# 회귀선이 있는 산점도: fit_reg=True (dafault)
sns.regplot(x='age',        #x축 변수
            y='fare',       #y축 변수
            data=titanic,   #데이터
            ax=ax1)         #axe 객체 - 1번째 그래프 

# 회귀선이 없는 산점도: fit_reg=False
sns.regplot(x='age',        #x축 변수
            y='fare',       #y축 변수
            data=titanic,   #데이터
            ax=ax2,         #axe 객체 - 2번째 그래프        
            fit_reg=False)  #회귀선 미표시

plt.show()