# -*- coding: utf-8 -*-
#4-24. 파이 차트 :.plot(kind='pie')
#각 변수에 속하는 데이터 값의 크기를 조각의 크기로 나타냄
#line 19부터


# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

plt.style.use('default')   # 스타일 서식 지정

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터 개수 카운트를 위해 모든 행에 대하여 값 1을 가진 열을 추가 
df['count'] = 1 #그룹화 후 합계 연산 시 각 그룹별로 count값이 합해짐--> 해당 그룹의 데이터 수를 의미
df_origin = df.groupby('origin').sum()   # origin 열을 기준으로 그룹화(origin 열의 값에 따라 행을 구분), 각 그룹별 합계 연산
print(df_origin.head())                  # 그룹 연산 결과 출력

# 제조국가(origin) 값을 실제 지역명으로 변경
df_origin.index = ['USA', 'EU', 'JAPAN']

# 제조국가(origin) 열에 대한 파이 차트 그리기 – count 열 데이터 사용
df_origin['count'].plot(kind='pie', 
                     figsize=(7, 5),
                     autopct='%1.1f%%',   # 퍼센트 % 표시(자동연산 autopercent), 소수점 이하 첫째자리까지 표시
                     startangle=10,       # 파이 조각을 나누는 시작점(각도 표시)
                     colors=['chocolate', 'bisque', 'cadetblue']    # 색상 리스트
                     )

plt.title('Model Origin', size=20)
plt.axis('equal')    # 파이 차트의 비율을 같게 (원에 가깝게) 조정
plt.legend(labels=df_origin.index, loc='upper right')   # 범례 표시
plt.show()