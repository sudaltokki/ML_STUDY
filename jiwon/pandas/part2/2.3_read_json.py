# -*- coding: utf-8 -*-

import pandas as pd

'''
JSON 파일(확장자: .json)은 데이터 공유를 목적으로 개발된 특수한 파일 형식
파이썬 딕셔너리 형식과 비슷하게 'key : value' 구조를 갖는데,
구조가 중첩되는 방식에 따라 옵션을 다르게 적용한다 (?)
'''

# read_json() 함수로 JSON 파일을 데이터프레임으로 변환
df = pd.read_json('./read_json_sample.json')
print(df)
print('\n')
print(df.index)