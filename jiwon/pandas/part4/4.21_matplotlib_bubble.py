# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'accerleration', 'model year', 'origin', 'name']

'''
버블 차트
실러더 개수를 3번째 변수로 추가
실린더 개수를 나타내는 정수를 그대로 사용하는 대신, 해당 열의 상대적 크기를 나타내는 비율을 꼐산
cylinders_size는 0~1 범위의 실수 값의 시리즈
점의 크기를 정하는 s 옵션에 cylinders_size를 입력해 값의 크기에 따라 점의 크기를 값에 따라 다르게 표
'''
# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
cylinders_size = df.cylinders / df.cylinders.max() * 300

# 3개의 변수로 산점도 그리기
df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=cylinders_size, alpha=0.3, figsize=(10, 5))
plt.title('Scatter Plot - mpg-weight-cylinders')
plt.show()

