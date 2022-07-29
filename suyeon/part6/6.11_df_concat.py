# -*- coding: utf-8 -*-
#4. 데이터 프레임 합치기
# 데이터(데이터프레임)가 여러 군데 나누어져 있을 때 하나로 합치거나 데이터를 연결하는 경우
# concat(), merge(), join()

#4-1. 데이터프레임 연결 : pd. concat(데이터프레임의 리스트)
# 서로 다른 데이터프레임들의 구성 형태와 속성 동일 시, 행/열 중 어느 방향으로 연결해도 일관적
# 기존 데이터 프레임의 형태 유지하면서 이어붙이는 경우: concat(데이터프레임을 원소로 갖는 리스트)

#concat: df와 df연결, df와 series, series와 series 연결 가능(단 리스트로 전달)

# 라이브러리 불러오기
import pandas as pd

# 데이터프레임 만들기
df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index=[0, 1, 2, 3])
 
df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index=[2, 3, 4, 5])

print(df1, '\n')
print(df2, '\n')

#데이터 프레임과 데이터 프레임 연결

# 2개의 데이터프레임을 위 아래 행 방향으로 이어 붙이듯 연결하기 
result1 = pd.concat([df1, df2])
# 결과 데이터 프레임: 행 인덱스는 그대로 유지
# 연결 방향: default axis=0: 위 아래, 행 방향으로 연결 (세로로 길게 연결)

# 행/열 이름:기존의 df에 존재하지 않는 행/열이 생기는 경우:
# 두 df의 합집합으로 구성 (default: join='outer')  (join='inner' 시 교집합으로 구성)

# 데이터값: 새 df에서 데이터가 없는 경우(어느 한쪽에만 데이터가 존재했던 경우) NaN으로 입력(0부터 3행의 d열)
print(result1, '\n')


# ignore_index=True 옵션 설정하기 : 기존 행 인덱스 무시, 새로운 정수형 위치 행 인덱스 설정
result2 = pd.concat([df1, df2], ignore_index=True)
print(result2, '\n')

# 2개의 데이터프레임을 좌우 열 방향으로 이어 붙이듯 연결하기 : axis=1
result3 = pd.concat([df1, df2], axis=1)
#join='outer' default: 각 df의 행 인덱스의 합집합 구성
print(result3, '\n')

# join='inner' 옵션 적용하기(교집합)
#[0,1,2,3], [2,3,4,5] 중 교집합인 2,3 행으로만 구성
result3_in = pd.concat([df1, df2], axis=1, join='inner')
print(result3_in, '\n')


#데이터프레임과 시리즈를 좌우 열 방향으로 연결: df에 열 추가하는 것과 동
#시리즈의 이름이 df의 열 이름으로 변환
#df의 행 인덱스와 series의 인덱스가 동일한 경우 그대로 추가
#공통 인덱스가 없는 경우 NaN으로 입력

# 시리즈 만들기
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')  #name이 열 이름으로 들어감
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')

# 데이터프레임과 시리즈 연결
# df1과 sr1을 좌우 열 방향으로 연결하기
result4 = pd.concat([df1, sr1], axis=1)
print(result4, '\n')

# df2과 sr2을 좌우 열 방향으로 연결하기
result5 = pd.concat([df2, sr2], axis=1, sort=True)
# sort :부울. join이outer일 때 아직 정렬되지 않은 경우 비 연결 축을 정렬.
# https://www.delftstack.com/ko/api/python-pandas/pandas-concat-function/
print(result5, '\n')

#시리즈와 시리즈 연결
# sr1과 sr3을 좌우 열 방향으로 연결하기
result6 = pd.concat([sr1, sr3], axis=1)
print(result6, '\n')

result7 = pd.concat([sr1, sr3], axis=0)
print(result7, '\n')
