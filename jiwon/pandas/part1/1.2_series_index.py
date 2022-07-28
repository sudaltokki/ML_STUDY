# -*- coding: utf-8 -*-

import pandas as pd

# 리스트를 시리즈로 변환하여 변수 sr에 저장
# 리스트는 딕셔너리의 key처럼 인덱스로 변환될 값이 없기 때문에 디폴트로 정수형 위치 인덱스가 자동 지정된다.
list_data = ['2022-07-15', 3014, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# 인덱스 배열은 변수 idx에 저장, 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values

print(idx) # 0~4 범위의 정수를 갖는 RangeIndex 객체로 표시된
print('\n')
print(val)