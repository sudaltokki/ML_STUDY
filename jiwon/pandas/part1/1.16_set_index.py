# -*- coding: utf-8 -*-

import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 특정 열을 데이터프레임의 행 인덱스로 설정
ndf = df.set_index(['이름'])
print(ndf)
print('\n')

ndf2 = ndf.set_index('음악')
print(ndf2)
print('\n')

ndf3 = ndf.set_index(['수학','음악'])
print(ndf3)

# 원본 데이터프레임을 바꾸지 않고 새로운 데이터프레임 객체를 반환
# set_index() 메소드를 사용하여 행 인덱스를 새로 지정하면 기존 행 인덱스는 삭제된다.
