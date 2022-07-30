# -*- coding: utf-8 -*-

'''
Excel 파일로 저장하는 방법 - DataFrame객체.to_excel('파일이름(경로)')
'''

import pandas as pd

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ['A', 'A+', 'B'],
        'basic': ['C', 'B', 'B+'],
        'c++': ['B+', 'C', 'C+'],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

# to_excel() 메소드를 사용해 Excel 파일로 내보내기
df.to_excel("./df_sample.xlsx")