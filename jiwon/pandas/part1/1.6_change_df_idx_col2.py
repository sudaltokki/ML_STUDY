# -*- coding: utf-8 -*-

import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index = ['준서', '예은'],
                  columns = ['나이', '성별', '학교'])


# 데이터프레임 df 출력
print(df)
print('\n')

# rename() 메소드를 적용해 df의 열 이름과 행 인덱스 변경
# rename() 메소드를 적용하면 원본 객체를 직접 수정하는 것이 아니라 새로운 데이터프레임 객체를 반환한다.
# 원본 객체를 변경하려면 inplace=True 옵션을 사용해야한다.

# df의 열 이름 변경
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)

# df의 행 인덱스 변경
df.rename(index={'준서':'학생1', '예은':'학생2'}, inplace=True)

# 변경된 df 출력
print(df)
