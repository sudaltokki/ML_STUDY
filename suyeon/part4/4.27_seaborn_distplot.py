# -*- coding: utf-8 -*-
#히스토그램/커널 밀도 그래프 
#4-27
#밀도 그래프: sns.kdeplot(), 히스토그램: sns.histplot(), 둘다 표시한 분포표: sns.dist90


# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
 
# distplot : 커널 밀도 그래프와 히스토그램 함께 있는 형태
sns.distplot(titanic['fare'], ax=ax1) #hist=False 시 히스토그램 표시 제거, kde=False시 커널 밀도 그래프 표시 제거

# kdeplot :커널 밀도 그래프만 있는 그래프
sns.kdeplot(x='fare', data=titanic, ax=ax2) 

# histplot :히스토그램만 있는 그래프
sns.histplot(x='fare', data=titanic,  ax=ax3)        

# 차트 제목 표시
ax1.set_title('titanic fare - distplot')
ax2.set_title('titanic fare - kedplot')
ax3.set_title('titanic fare - histplot')

plt.show()