# -*- coding: utf-8 -*-

#4-22. 그래프를 그림 파일로 저장: .savefig(파일이름과 파일 경로)

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

# 3개의 변수로 산점도 그리기 
#cylinders_size를 점의 색깔로 표시
#값에 따라 다른 색 할당, cmap='': 색상 정하는 컬러맵 옵션
#marker='+' : 점을 십자모양으로 표시
df.plot(kind='scatter', x='weight', y='mpg', marker='+', figsize=(10, 5),
        cmap='viridis', c=cylinders_size, s=50, alpha=0.3)
plt.title('Scatter Plot: mpg-weight-cylinders')

plt.savefig("./scatter.png")   
plt.savefig("./scatter_transparent.png", transparent=True)   #transparent=True: 그림 배경을 투명하게 지정

plt.show()