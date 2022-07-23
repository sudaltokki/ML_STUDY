# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:23:43 2022

@author: user
"""

import pandas as pd

data={'name':['Jerry','Riah','Paul'],
      'algol':['A',"A+",'B'], 'basic':["C","B","B+"],
      'c++':['B+','C','C+']}

df=pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_csv('./df_sample.csv') #파이썬 실행 파일이 위치하고 있는 현재 디렉터리(./) 에 해당 파일명으로 생성하고 저장