# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns

# titanic 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정(5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 그래프 객체 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 그래프 그리기 - 선형회귀선 표시(fig_reg=True)
sns.regplot(x='age', # x축 변수
            y='fare', # y축 변수
            data=titanic, # 데이터
            ax=ax1) # axe 객체 - 1번째 그래프

# 그래프 그리기 - 선형회귀선 미표시(fig_rg=False)
sns.regplot(x='age',
            y='fare',
            data=titanic, 
            ax=ax2,
            fit_reg=False) # 회귀선 미표시

plt.show()

# 선형 회귀선이 뭐지?