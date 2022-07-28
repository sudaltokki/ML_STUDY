# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
exam_data = {'수학':[90, 80, 70], '영어':[98, 89, 95], 
             '음악':[85, 85, 100], '체육':[100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터프레임의 행 또는 열을 삭제하는 drop() 메소드
# 축 옵션을 별도로 입력하지 않거나, axis=0을 입력하면 행을 삭제한다.
# 데이터프레임 df를 복제하여 변수 df2에 저장, df2의 행(row) 1개 삭제
df2 = df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')

# 데이터프레임 df를 복제하여 변수 df3에 저장, df3의 행 2개 삭제
df3 = df[:]
df3.drop(['우현', '인아'], inplace=True)
print(df3)

