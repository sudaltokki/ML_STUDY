# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'accerleration', 'model year', 'origin', 'name']

'''
파이 차트 - 원을 파이 조각처럼 나누어서 표현
조각의 크기는 해당 변수에 속하는 데이터 값의 크기에 비례
plot() 메소드에 kind='pie' 옵션 사용
'''

# 데이터 개수 카운트를 위해 값 1을 가진 열 추가
df['count'] = 1
df_origin = df.groupby('origin').sum() # origin 열을 기준으로 그룹화, 합계 연산
print(df_origin.head())

# 제조국가(origin) 값을 실제 지역명으로 변경
df_origin.index = ['USA', 'EU', 'JPN']

# 제조국가 열에 대한 파이 차트 그리기 - count 열 데이터 이용
# autopct 옵션은 숫자를 퍼센트(%)로 표시하는데, 소수점 이하 첫째자리까지 표기한다는 뜻
# startangle 옵션은 조각을 나누는 시작점 (각도)
df_origin['count'].plot(kind='pie', figsize=(7, 5), autopct='%1.1f%%',
                        startangle=10, colors=['chocolate', 'bisque', 'cadetblue'])

plt.title('Model Origin', size=20)
plt.axis('equal') # 파이 차트의 비율을 같게(원에 가깝게) 조정
plt.legend(labels=df_origin.index, loc='upper right')
plt.show()