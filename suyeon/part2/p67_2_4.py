# -*- coding: utf-8 -*-
"""
p67-2-4
"""

import pandas as pd

url='./sample.html'

tables=pd.read_html(url) #여러개의 데이터프레임을 원소로 갖는 리스트로 저장됨

print(len(tables))
print('\n')

for i in range(len(tables)):
    print("tables[%s]" %i)  #파이썬 문법 다시 확인
    print(tables[i])
    print('\n')
    

df=tables[1]  #두번째 표를 인덱싱하여 df변수에 저장
df.set_index(['year'], inplace=True) #첫 인자 열을 행 인덱스로 설정, 원본 변환
print(df)
    