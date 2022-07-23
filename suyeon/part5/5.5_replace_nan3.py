# -*- coding: utf-8 -*-
#5-5. 이웃하고 있는 값으로 NaN 대체
#특성 상 이웃 데이터끼리 유사성 가질 가능성 높은 경우
#df.fillna(method='ffill') :해당 Nan행이 데이터를 그 직전 행에 있는 값으로 대체
#df.fillna(method='bfill') :해당 Nan행이 데이터를 바로 다음 행에 있는 값으로 대체




# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# embark_town 열의 829행의 NaN 데이터 출력
print(df['embark_town'][825:830])
print('\n')

# embark_town 열의 NaN값을 바로 앞에 있는 828행의 값으로 변경하기
df['embark_town'].fillna(method='ffill', inplace=True)
print(df['embark_town'][825:830])


#누락데이터가 NaN이 아니라 숫자 0이나 '?', '-' 등으로 표시된 경우
#replace() 이용하여 np.nan으로 변경
#import numpy as np 필요
#예)  df.replace("?", np.nan, inplace=True)