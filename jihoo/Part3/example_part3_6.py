# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 02:30:15 2022

@author: user
"""


import pandas as pd

df = pd.read_excel('C:\\Python_exfiles\\part3/남북한발전전력량.xlsx', engine='openpyxl')

df_ns = df.iloc[[0,5],3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)

tdf_ns = df_ns.T
tdf_ns.plot(kind = 'hist')

# TypeError: no numeric data to plot