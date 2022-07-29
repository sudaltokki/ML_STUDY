# -*- coding: utf-8 -*-
#2-3. 다중 회귀 분석 Multivariate Regression
# 여러개의 독립 변수가 종속 변수에 영향을 주고 선형 관계를 갖는 경우 사용(지도 학습; 실제 종속변수 데이터 알고 있는 상태에서 학습하므로)
# 각 독립 변수의 계수와 상수항에 적절한 값을 찾아 모형 완성(Y=b+a1x1+a2X2+''')


### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
[Step 1 ~ 3] 데이터 준비 
'''
# CSV 파일을 데이터프레임으로 변환
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# horsepower 열의 자료형 변경 (문자열 ->숫자)
df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환

# 분석에 활용할 열(속성)을 선택 (연비, 실린더, 출력, 중량)
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]


'''
Step 4: 데이터셋 구분 - 훈련용(train data)/ 검증용(test data)
'''

# 속성(변수) 선택: 여러개의 독립변수, x: dataframe
X=ndf[['cylinders', 'horsepower', 'weight']]  #독립 변수 X1, X2, X3
y=ndf['mpg']     #종속 변수 Y

# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10) 

print('훈련 데이터: ', X_train.shape)
print('검증 데이터: ', X_test.shape)   
print('\n') 


'''
Step 5: 다중회귀분석 모형 - sklearn 사용 (모형 학습 및 검증)
'''

# sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()   

# train data를 가지고 모형 학습
lr.fit(X_train, y_train)

# 학습을 마친 모형에 test data(검증 데이터)를 적용하여 결정계수(R-제곱) 계산 (훈련데이터 제외)
r_square = lr.score(X_test, y_test) #평가 지표 결정계수
print(r_square)
print('\n')

# 회귀식의 기울기
print('X 변수의 계수 a: ', lr.coef_) #리스트 형태로 반환[, ,]
print('\n')

# 회귀식의 y절편
print('상수항 b', lr.intercept_)
print('\n')

#모형이 예측한 결과와 실제 값 비교
# train data의 산점도와 test data로 예측한 회귀선을 그래프로 출력 
y_hat = lr.predict(X_test) #모형 예측값 저장

plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y_test, label="y_test") #실제 예측값
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
plt.legend() # plt.legend():   https://pyvisuall.tistory.com/55
plt.show()
# 단순 회귀 분석에 비해 덜 뾰족하지만(첨도가 누그러짐)(7-1), 
#다항 회귀 분석에 비해서는 두 그래프가 편향된 정도가 더 큰 듯(7-2)