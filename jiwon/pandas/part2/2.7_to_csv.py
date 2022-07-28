# -*- coding: utf-8 -*-

'''
판다스 데이터프레임은 2차원 배열로 구조화된 데이터이기 때문에 2차원 구조를 갖는 CSV 파일로 변환 가능
방법 - DataFrame객체.to_csv('파일이름(경로)')
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

# to_csv() 메소드를 사용해 CSV 파일로 내보내기
df.to_csv("./df_sample.csv")
