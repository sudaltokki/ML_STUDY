# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns

# titanic 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정(5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 그래프 객체 생성
fig = plt.figure(figsize=(15, 5))

'''
Seaborn 라이브러리는 히트맵(heatmap)을 그리는 heatmap() 메소드 제공
2개의 범주형 변수를 각각 x, y축에 놓고 데이터를 매트릭스 형태로 분류
데이터프레임을 피벗테이블로 정리할 때 한 변수('sex'열)를 행 인덱스로, 
나머지 변수('class'열)를 열 이름으로 설정
'''

# 피벗테이블로 범주형 변수를 각각 행, 열로 재구분하여 정리
# aggfunc='size'는 데이터 값의 크기를 기준으로 집계한다는 뜻의 옵션
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')

# 히트맵 그리기
sns.heatmap(table, # 데이터프레임
            annot=True, fmt='d', # 데이터 값 표시 여부, 정수형 포맷
            cmap='YlGnBu', # 컬러 맵
            linewidth=.5, # 구분 선
            cbar=False) # 컬러 바 표시 여부

plt.show()