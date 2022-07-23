# -*- coding: utf-8 -*-
#5-7. 중복 데이터 제거
#df.drop_duplicates() : inplace=True시 원본 객체 변경
#중복 행 중 먼저 나오는 행만 남음.


# 라이브러리 불러오기
import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
print(df)
print('\n')

# 데이터프레임에서 중복 행을 제거
df2 = df.drop_duplicates()
print(df2)
print('\n')

# c2, c3열을 기준으로 중복 행을 제거: subset=['',''] 열 이름의 리스트 전달
df3 = df.drop_duplicates(subset=['c2', 'c3'])
# 각 행에 대하여, subset에 속하는 열의 값에 대해서만 중복데이터 찾고 삭제
#(출력 시에는 subset에 속하지 않는 열의 값도 그대로 출력. 남아있음.)

print(df3)
