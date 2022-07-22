# -*- coding: utf-8 -*-
#1-5. 산점도 그리기 :.plot(kind='scatter')
# 서로 다른 두 변수 사이 관계
#.plot(kind='line', 'o')와 사실상 동일

# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')   # 스타일 서식 지정

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 연비(mpg)와 차중(weight) 열에 대한 산점도 그리기
df.plot(kind='scatter', x='weight', y='mpg',  c='coral', s=10, figsize=(10, 5))
#x,y: df에서 각 변수로 지정할 서로 다른 두 열 선택, c: color, s:size
plt.title('Scatter Plot - mpg vs. weight')
plt.show()