# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 07:07:04 2022

@author: user
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

g = sns.FacetGrid(data=titanic, col = 'who', row = 'survived')

g = g.map(plt.hist,'age')