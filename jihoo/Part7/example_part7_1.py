# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 02:07:17 2022

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\Python_exfiles\part6/auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

print(df.head())
print('\n')

pd.set_option('display.max_columns', 10)
print(df.head())

print(df.info())
print('\n')

print(df.describe())

print(df['horsepower'].unique())
print('\n')
df['horsepower'].replace('?',np.nan, inplace=True)
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
df['horsepower'] = df['horsepower'].astype('float')

print(df.describe())

ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print(ndf.head())

ndf.plot(kind = 'scatter', x='weight', y='mpg', c='coral', s=10, figsize = (10,5) )
plt.show()
plt.close()

fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x='weight', y='mpg', data = ndf, ax = ax1)
sns.regplot(x='weight', y='mpg', data = ndf, ax = ax2, fit_reg = False)
plt.show()
plt.close()

sns.jointplot(x='weight', y='mpg', data = ndf)
sns.jointplot(x='weight', y='mpg', kind = 'reg', data = ndf)
plt.show()
plt.close()

grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()

x=ndf[['weight']]
y=ndf['mpg']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3, random_state = 10)
print('train data 개수 : ', len(x_train))
print('test data 개수 : ', len(x_test))

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)

r_square = lr.score(x_test, y_test)
print(r_square)

print('기울기 a : ', lr.coef_)
print('\n')

print('y절편 b : ', lr.intercept_)
y_hat = lr.predict(x)

plt.figure(figsize = (10,5))
ax1 = sns.kdeplot(y, label = "y")
ax2 = sns.kdeplot(y_hat, label = "y_hat", ax=ax1)
plt.legend()
plt.show()