# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns

# titanic 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정(5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 그래프 객체 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

'''
범주형 데이터의 산점도 - 범주형 변수에 들어 있는 각 범주별 데이터의 분포를 확인하는 방법이다.
stripplot() 함수와 swarmplot() 함수를 사용할 수 있다
swarmplot() 함수는 데이터의 분산까지 고려하여 데이터 포인트가 서로 중복되지 않고
데이터가 퍼져있는 정도를 입체적으로 볼 수 있도록 그린다.

hue='sex' 옵션을 추가하면 'sex'열의 데이터 값인 성별을 색상으로 구분하여 출력한다
'''

# 이산형 변수의 분포 - 데이터 분산 미고려
sns.stripplot(x='class', 
              y='age',
              data=titanic,
              ax=ax1)

# 이산형 변수의 분포 - 데이터 분산 고려(중복X)
sns.stripplot(x='class', 
              y='age',
              data=titanic,
              hue='sex', # 성별을 색상으로 구분하여 출력
              ax=ax2)

# 차트 제목 표시
ax1.set_title('Strip Plot')
ax2.set_title('Strip Plot')

plt.show()