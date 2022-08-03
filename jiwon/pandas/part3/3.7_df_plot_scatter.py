# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

'''
2개의 열을 선택하여 두 변수의 관계를 나타내는 산점도

산점도를 보면 차량의 무게가 클수록 연비는 전반적으로 낮아지는 경향을 보인다.
차량의 무게와 연비는 역의 상관관계를 갖는다고 해석할 수 있다
'''
df.plot(x='weight', y='mpg', kind='scatter')

