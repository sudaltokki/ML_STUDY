# -*- coding: utf-8 -*-
#5-4: 최빈값으로 NaN 치환


# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# embark_town 열의 825~829 행의 NaN 데이터 출력
print(df['embark_town'][825:830]) #행, 열 순서 바뀌어도 각 인덱스와 이름으로 구분되므로 상관 없는 듯
print('\n')
"""print(df[825:830]['embark_town']) 
print('\n')"""  #위와 동일 series 출력

# embark_town 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()   
#.value_counts: 승선 도시 별 승객 수 찾기
#df.idmax: 가장 큰 값을 갖는 도시 찾기 
#idmax: 가장 큰 값 갖는 원소의 인덱스 반환, 여러개이면 여러개 반환 (https://nomalcy.tistory.com/39)

print(most_freq) #idmax에서 인덱스를 반환하므로, southhampton 반환
print('\n')

df['embark_town'].fillna(most_freq, inplace=True) #최빈값으로 NaN 대체
#승선도시 NaN이었던 행의 인덱스가 모두 최빈 인덱스인 southhampton으로 대체

# embark_town 열 825~829행의 NaN 데이터 출력 (NaN 값이 most_freq 값으로 대체)
print(df['embark_town'][825:830])