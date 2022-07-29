# -*- coding: utf-8 -*-
#2-2. 다항 회귀 분석 polynomial regression
# 2차함수 이상의 다항함수를 이용하여 두 변수간의 선형 관계 설명하는 알고리즘
# 두 변수간의 상관관계가 존재하지만, 직선보다는 곡선이 적합한 경우
# 3개의 계수 a,b,c 이용 모형 완성

### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
[Step 1 ~ 4] 데이터 준비 (line 41까지 이전과 동일)
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

# ndf 데이터를 train data 와 test data로 구분(7:3 비율)
X=ndf[['weight']]  #독립 변수 X
y=ndf['mpg']     #종속 변수 Y

# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10) 

print('훈련 데이터: ', X_train.shape) # .shape: numpy array로 만든 행과 열의 개수 카운트
# https://scribblinganything.tistory.com/484#:~:text=Shpae%20%ED%95%A8%EC%88%98%EB%8A%94%20numpy%20array%20%EB%A1%9C%20%EB%A7%8C%EB%93%A0%20%ED%96%89%EB%A0%AC%EC%9D%98%20%ED%96%89%EC%9D%98,%EA%B0%99%EC%8A%B5%EB%8B%88%EB%8B%A4.%20tuple%20%EA%B0%92%20%28%ED%96%89%2C%EC%97%B4%29%20%3D%20numpy.shape%20%28numpy%20array%29
print('검증 데이터: ', X_test.shape)   
print('\n')


'''
Step 5: 비선형회귀분석 모형 - sklearn 사용 (모형 학습 및 검증)
'''

# sklearn 라이브러리에서 필요한 모듈 가져오기 
from sklearn.linear_model import LinearRegression      #선형회귀분석
from sklearn.preprocessing import PolynomialFeatures   #다항식 변환

# 다항식 변환 
#2차항 객체 poly 생성
poly = PolynomialFeatures(degree=2) 

#X_train 데이터를 2차항으로 변형: poly.fit_transform(x_train)
X_train_poly=poly.fit_transform(X_train) 

print('원 데이터: ', X_train.shape) #열 개수:1
print('2차항 변환 데이터: ', X_train_poly.shape)  #열의 개수가 3개로 늘어남
print('\n')

# train data를 가지고 모형 학습
pr = LinearRegression()   #회귀분석 모형 객체 생성, pr에 저장
pr.fit(X_train_poly, y_train) # pr.fit(2차항 변형 x 데이터, y): 2차 모델 훈련

# 학습을 마친 모형에 test data를 적용하여 결정계수(R-제곱) 계산
#X_test 데이터를 2차항으로 변형: poly.fit_transform(x_test)
X_test_poly = poly.fit_transform(X_test)  

r_square = pr.score(X_test_poly,y_test) #poly.score(): 검증데이터 이용, 모형의 예측 능력평가
print(r_square)
print('\n')


# train data의 산점도와 test data로 예측한 회귀선을 그래프로 출력 
#학습된 모형의 예측
y_hat_test = pr.predict(X_test_poly)

# 학습 회귀 선과 훈련 데이터의 분포 비교
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(X_train, y_train, 'o', label='Train Data')  # 데이터 분포
#????????/여기서 오류남...
ax.plot(X_test, y_hat_test, 'r+', label='Predicted Value') # 모형이 학습한 회귀선: 점 십자 모양
    # 하나의 평면에 두개 그래프 그리고 싶을 때 fig.add_subplot(1, 1, 1) 설정 후 
    #하나의 ax객체에 plot 2번 적용
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()
plt.close()

# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교 
X_ploy = poly.fit_transform(X) #전체 X자체를 2차형으로 변환
y_hat = pr.predict(X_ploy) # 전체 X_poly에 대해 모형이 예측한 값

plt.figure(figsize=(10, 5)) #seaborn의 displot() 이용, 실제 값y와 예측값y_hat 비교
ax1 = sns.kdeplot(y, label="y")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
plt.legend()
plt.show()

# .plot 이용 산점도를 하나 평면에 두개: line 82~92 
# sns.displot 이용 회귀선을 하나 평면에 두개: line 95~102