# -*- coding: utf-8 -*-
"""p33, 1-13"""

import pandas as pd

exam_data={'이름':['서준','우현','인아'],
           '수학':[90,80,70], '영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}

df=pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
"""해당 열의 column name 은 보여는 지되, 해당 df에서 어느 행의 index 로도 사용되지 않음"""

print(df)

df.loc[3]="테스트용3"
df.loc["4"]="테스트용4" 
df.iloc[5]="테스트용5"
print(df)
print(type(df.index))