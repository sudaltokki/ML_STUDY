# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'accerleration', 'model year', 'origin', 'name']

# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
cylinders_size = df.cylinders / df.cylinders.max() * 300

# 3개의 변수로 산점도 그리기
df.plot(kind='scatter', x='weight', y='mpg', marker='+', c=cylinders_size, cmap='viridis',
        s=50, alpha=0.3, figsize=(10, 5)) # cmap-색상을 정하는 컬러맵 옵션
plt.title('Scatter Plot - mpg-weight-cylinders')

# 그래프를 그림 파일로 저장
plt.savefig("./scatter.png")
plt.savefig("./scatter_transparent.png", transparent=True) # 그림 배경을 투명하게 지정
plt.show()
