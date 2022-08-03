# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:13:50 2022

@author: user
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

pd.set_option('display.max_columns', 15)

rdf = df.drop(['deck','embark_town'], axis = 1)

rdf = rdf.dropna(subset = ['age'], how = 'any', axis = 0)

most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
rdf['embarked'].fillna(most_freq, inplace = True)

ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]

onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix = 'town')
ndf = pd.concat([ndf,onehot_embarked], axis = 1)

ndf.drop(['sex', 'embarked'], axis = 1, inplace = True)

X=ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 
       'town_C', 'town_Q', 'town_S']]
Y=ndf['survived']

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.3, random_state = 10)

print('train data 개수 : ', X_train.shape)
print('test data 개수 : ', X_test.shape)

from sklearn import svm

svm_model = svm.SVC(kernel = 'rbf')

svm_model.fit(X_train, Y_train)

Y_hat = svm_model.predict(X_test)

print(Y_hat[0:10])
print(Y_test.values[0:10])

from sklearn import metrics

svm_matrix = metrics.confusion_matrix(Y_test, Y_hat)
print(svm_matrix)
print('\n')

svm_report = metrics.classification_report(Y_test, Y_hat)
print(svm_report)