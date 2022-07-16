# -*- coding: utf-8 -*-
"""
p43, 1-19
"""
import pandas as pd

dict_data={'c0':[1,2,3], 'c1':[4,5,6],'c2':[7,8,9],'c3':[13,14,15]}

df=pd.DataFrame(dict_data, index=['r0','r1','r2'])
df1=pd.DataFrame(dict_data, index=['ㄱ','ㄴ','ㄷ']) 
df2=pd.DataFrame(dict_data, index=['ㄱ3','ㄴ2','ㄷ1']) """이 경우 한글 순으로 정렬, 먼저 생기는 순서로 나열"""
print(df)
print('\n')

ndf=df.sort_index(ascending= False)
print(ndf)
print(df1.sort_index(ascending= False)) 
print(df2.sort_index(ascending= False)) 
