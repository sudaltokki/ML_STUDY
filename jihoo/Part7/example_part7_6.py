# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:49:33 2022

@author: user
"""

import pandas as pd
import numpy as np

uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)

df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial', 
              'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']

pd.set_option('display.max_columns',15)

print(df.head())
print('\n')

print(df.info())
print('\n')

print(df.describe())

print(df['bare_nuclei'].unique())
print('\n')

df['bare_nuclei'].replace('?', np.nan, inplace=True)
df.dropna(subset = ['bare_nuclei'], axis = 0, inplace = True)
df['bare_nuclei'] = df['bare_nuclei'].astype('int')

print(df.describe())

X=df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial', 
        'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]
Y=df['class']

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=10)

print('train data 개수 : ', X_train.shape)
print('test data 개수 : ', X_test.shape)

from sklearn import tree

tree_model = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 5)
tree_model.fit(X_train, Y_train)

Y_hat = tree_model.predict(X_test)

print(Y_hat[0:10])
print(Y_test.values[0:10])

from sklearn import metrics
tree_matrix = metrics.confusion_matrix(Y_test, Y_hat)
print(tree_matrix)
print('\n')

tree_report = metrics.classification_report(Y_test, Y_hat)
print(tree_report)
