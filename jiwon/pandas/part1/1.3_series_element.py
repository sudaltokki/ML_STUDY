# -*- coding: utf-8 -*-

import pandas as pd

# 투플을 시리즈로 변화(인덱스 옵션 지정)
tup_data = ('지원', '2000-06-05', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

# 원소를 1개 선택
print(sr[0])
print(sr['이름'])

# 여러 개의 원소를 선택(인덱스를 리스트 형태로 입력)
print(sr[[1, 2]])
print('\n')
print(sr[['생년월일', '성별']])

# 여러 개의 원소를 선택(인덱스 범위 지정)
print(sr[1 : 2])
print('\n')
print(sr['생년월일' : '성별'])