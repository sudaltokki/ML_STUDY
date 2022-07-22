# -*- coding: utf-8 -*-
#1-4. 히스토그램 : 변수가 하나인 단변수 데이터의 빈도수를 그래프로 표현
#구간을 나누는 간격의 크기에 따라 빈도, 히스토그램의 모양 결정
#df.plot(kind='hist')


# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')   # 스타일 서식 지정

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 연비(mpg) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))
#bins='': 구간의 개수 설정

# 그래프 꾸미기
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()