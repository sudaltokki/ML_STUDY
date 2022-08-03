# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'accerleration', 'model year', 'origin', 'name']

'''
히스토그램은 변수가 하나인 단변수 데이터의 '빈도수'를 그래프로 표현
x축을 같은 크기의 여러 구간으로 나누고 각 구간에 속하는 데이터 값의 개수(빈도)를 y축에 표시
구간을 나누는 간격의 크기에 따라 빈도가 달라지고 히스토그램의 모양이 변한다.
'''

# 연비(mpg) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))

# 그래프 꾸미기
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()