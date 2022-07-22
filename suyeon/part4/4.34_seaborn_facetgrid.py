# -*- coding: utf-8 -*-
#4-34. 조건을 적용하여 화면을 그리드로 분할하기: sns.Facetgrid()
#sns.Facetgrid(): 행,열 방향으로 서로 다른 조건을 적용하여 여러개의 서브플롯을 만들고,
#각 서브 플롯에 적용할 그래프의 종류를 map() 이용하여 그리드 객체에 전달


# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 조건에 따라 그리드 나누기: 축 데이터와 서브 플롯 개수 결정
g = sns.FacetGrid(data=titanic, col='who', row='survived') 
#'who'의 데이터 종류: woman, man, child 3가지, 'survived': 1,0 2가지
#총 3*2, 6개의 서브플롯 생성
#각 서브플롯마다 행,열의 데이터 종류 조합을 다르게 하여 해당하는 데이터를 축으로 갖게 생성

# 그래프 적용하기: 플롯에 데이터 값으로 들어갈 열과, 그래프 종류 결정 
g = g.map(plt.hist, 'age') #'age'열의 데이터 기준 히스토그램을 그림
