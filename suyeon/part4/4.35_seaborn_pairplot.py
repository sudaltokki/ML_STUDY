# -*- coding: utf-8 -*-
#4-35. 이변수 데이터의 분포: sns.pairplot()
# 인자로 전달되는 df의 열(변수)의 가능한 모든 2개씩의 조합에 대한 그래프 표현

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# titanic 데이터셋 중에서 분석 데이터 선택하기-새 데이터 프레임으로 전달
titanic_pair = titanic[['age','pclass', 'fare']]
print(type(titanic_pair))
#3개 변수에 대해, 가능한 모든 pair조합: 3*3, 9개 서브 플롯 생성

# 조건에 따라 그리드 나누고, 그래프 그리기
g = sns.pairplot(titanic_pair)
#같은 변수끼리 짝인 경우(오른쪽 아래로 향하는 대각선): 히스토그램
#서로 다른 변수간 : 산점도
