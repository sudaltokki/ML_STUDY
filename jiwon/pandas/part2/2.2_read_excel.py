# -*- coding: utf-8 -*-

import pandas as pd

# read_excel() 함수로 Excel 파일을 데이터프레임으로 변환
file_path = './남북한발전전력량.xlsx'
df1 = pd.read_excel(file_path)
df2 = pd.read_excel(file_path, header=None)

print(df1)
print('\n')
print(df2) # header=None 옵션을 사용하면 정수현 인덱스를 열 이름으로 자동 할당

