# -*- coding: utf-8 -*-

'''
여러 개의 데이터프레임을 하나의 Excel 파일로 저장하는 방법 - pandas.ExcelWriter('파일이름(경로)')

판다스 ExcelWriter() 함수는 Excel 워크북 객체(Excel 파일)를 생성한다.
데이터프레임에 to_excel() 메소드를 적용할 때 삽입하려는 워크북 객체를 인자로 전달
sheet_name 옵션을 통해 시트 이름을 다르게 설정하면, 
같은 파일의 서로 다른 시트에 여러 데이터프레임을 구분하여 저장한다.
'''

import pandas as pd

data1 = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ['A', 'A+', 'B'],
        'basic': ['C', 'B', 'B+'],
        'c++': ['B+', 'C', 'C+'],}

data2 = {'c0':[1, 2, 3],
         'c1':[4, 5, 6],
         'c2':[7, 8, 9],
         'c3':[10, 11, 12],
         'c4':[13, 14, 15],}

df1 = pd.DataFrame(data1)
df1.set_index('name', inplace=True)
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)
print(df2)

# df1을 'sheet1'으로 df2를 'sheet2'로 저장
writer = pd.ExcelWriter('./df_excelwriter.xlsx')
df1.to_excel(writer, sheet_name='sheet1')
df2.to_excel(writer, sheet_name='sheet2')
writer.save()
