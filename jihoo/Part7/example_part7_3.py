# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 09:53:42 2022

@author: user
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\Python_exfiles\part7/auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?',np.nan, inplace=True)
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
df['horsepower'] = df['horsepower'].astype('float')

ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]

x=ndf[['cylinders', 'horsepower','weight']]
y=ndf['mpg']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3, random_state = 10)

print('훈련 데이터: ', x_train.shape)
print('검증 데이터: ', x_test.shape)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train, y_train)

r_square = lr.score(x_test, y_test)
print(r_square)
print('\n')

print('X 변수의 계수 a : ', lr.coef_)
print('\n')

print('상수항 b : ', lr.intercept_)

y_hat = lr.predict(x_test)

plt.figure(figsize = (10,5))
ax1 = sns.kdeplot(y_test, label = "y_test")
ax2 = sns.kdeplot(y_hat, label = "y_hat", ax=ax1)
plt.legend()
plt.show()