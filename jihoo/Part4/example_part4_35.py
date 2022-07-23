# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 07:09:45 2022

@author: user
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

titanic_pair = titanic[['age', 'pclass', 'fare']]

g = sns.pairplot(titanic_pair)