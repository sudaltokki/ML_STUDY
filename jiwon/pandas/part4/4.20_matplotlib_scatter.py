# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'accerleration', 'model year', 'origin', 'name']

'''
산점도(scatter plot)는 서로 다른 두 변수 사이의 관계를 나타낸다.
이때 각 변수는 연속되는 값을 갖는다. 일반적으로 정수형 또는 실수형
2개의 연속 변수를 각각 x축과 y축에 하나씩 놓고, 좌표를 점으로 표시

두 연속 변수의 관계를 보여준다는 점에서 선 그래프와 비슷하다
선그래프를 그릴때 plot()메소드에 'o'옵션을 적용하면 선 없이 점으로만 표현되는데, 사실상 산점도와 같다
'''

# 연비(mpg)와 차중(weight) 열에 대한 산점도 그리기
# c 옵션은 점의 색상, s 옵션은 점의 크기
df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10, 5))
plt.title('Scatter Plot - mpg vs weight')
plt.show()