# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use('seaborn-poster')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'accerleration', 'model year', 'origin', 'name']

# 그래프 객체 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# axe 객체에 boxplot 메소드로 그래프 출력 (수직 박스 플롯, 수평 박스 플롯)
ax1.boxplot(x=[df[df['origin']==1]['mpg'], # USA의 mpg 범위
              df[df['origin']==2]['mpg'], # EU의 mpg 범위
              df[df['origin']==3]['mpg']], # JAPAN의 mpg 범위
            labels=['USA', 'EU', 'JAPAN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
              df[df['origin']==2]['mpg'],
              df[df['origin']==3]['mpg']],
            labels=['USA', 'EU', 'JAPAN'], vert=False) # 수평 박스 플롯 그리기

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

# 파이썬 그래프 갤러리에서 파이썬으로 그릴 수 있는 다양한 그래프와 설정 옵션을 참조할 수 있다.