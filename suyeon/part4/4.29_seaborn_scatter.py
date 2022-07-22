# -*- coding: utf-8 -*-
#4-29. 범주형 데이터의 산점도
#stripplot()
#swarmplot() : 데이터의 분산까지 고려하여 표시, 데이터 포인트가 서로 중복되지 않게 그림

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
 
# 이산형 변수의 분포 - 데이터 분산 미고려(중복 표시 존재): stripplot
sns.stripplot(x="class",      #x축 변수
              y="age",        #y축 변수           
              data=titanic,   #데이터셋 - 데이터프레임
              ax=ax1)         #axe 객체 - 1번째 그래프 

# 이산형 변수의 분포 - 데이터 분산 고려 (중복 X) :swarmplot
sns.swarmplot(x="class",      #x축 변수
              y="age",#y축 변수
              hue='sex',# hue 는 새로운 변수를 다른 색상을 이용하여 추가하는 파라미터 (https://kimdingko-world.tistory.com/170)
              data=titanic,   #데이터셋 - 데이터프레임
              ax=ax2)         #axe 객체 - 2번째 그래프     

#hue='sex' 옵션을 위 두 함수에 추가 시, 'sex'열의 데이터 값인 남녀 성별을 색상으로 구분   

# 차트 제목 표시
ax1.set_title('Strip Plot')
ax2.set_title('Strip Plot')

plt.show()