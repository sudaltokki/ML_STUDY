# -*- coding: utf-8 -*-
#4-21 버블차트

# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')   # 스타일 서식 지정

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
cylinders_size = df.cylinders / df.cylinders.max() * 300
#.max() : itrable한 데이터의 최대값 반환 (https://blockdmask.tistory.com/411)
#위의 코드: 모든 행에 대한 연산값을 시리즈로 반환

# 3개의 변수로 산점도 그리기 : 세번째 변수는 점의 사이즈로 표현
df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10, 5),
        s=cylinders_size, alpha=0.3)
plt.title('Scatter Plot: mpg-weight-cylinders')
plt.show()