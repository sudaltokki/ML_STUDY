# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 07:03:14 2022

@author: user
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')

sns.heatmap(table, annot=True, fmt = 'd', cmap = 'YlGnBu',
            linewidth=.5, cbar=False)

plt.show()