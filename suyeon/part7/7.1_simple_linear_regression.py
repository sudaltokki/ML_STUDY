# -*- coding: utf-8 -*-
#2. 회귀 분석
# 가격, 주가, 환율 등 연속적 값을 갖는 연속변수 예측하는데 주로 활용
# dependent variable(predictor): 분석 모형이 예측하고자 하는 목표
# independent variable(explanatory ''): 예측을 위해 모형이 사용하는 속성

#2-1. 단순 회귀 분석
# 두 변수 사이에 일대이롤 대응되는 확률적, 통계적 상관성을 찾는 알고리즘(대표적 지도학습)
# 변수 X,Y를 가지고, 일차방정식의 계수 a,b를 반복학습으로 찾는 과정 (선형 관계)

### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
[Step 1] 데이터 준비 - read_csv() 함수로 자동차 연비 데이터셋 가져오기
'''
# CSV 파일을 데이터프레임으로 변환
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# 데이터 살펴보기
print(df.head())   #처음부터 10개 열 나오는데 왜그러는지??
print('\n')

#  IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns', 10)
print(df.head())   
print('\n')


'''
[Step 2] 데이터 탐색
'''

# 데이터 자료형 확인
print(df.info())  
print('\n')

# 데이터 통계 요약정보 확인
print(df.describe())
print('\n')
#horsepower열에서만 통계 요약 없음--> 숫자 형이 아닌 문자열, 마력이므로 숫자형이 더 적절하므로 변환 필요

# horsepower 열의 자료형 변경 (문자열 ->숫자)
print(df['horsepower'].unique())          # horsepower 열의 고유값 확인
print('\n')

df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경: df[].replace(바꿔야할 것,바꿀 것,inplace=원본 변환 여부)

df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제: df.dropna(열 지정, 행에 대해 삭제, 원본 변환 여부 )

df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환: df[].astype()

print(df.describe())                                     # 데이터 통계 요약정보 확인
print('\n')

#이제 horsepower열에서도 연산값 계산 가능

'''
[Step 3] 속성(feature 또는 variable) 선택
'''

# -분석에 활용할 열(속성)을 선택 (연비, 실린더, 출력, 중량)
# 예측목표인 종속 변수Y가 될 mpg열과, 독립변수X 후보인 나머지 3개 열
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']] #df[[]] : ndf: dataframe
print(ndf.head())   
print('\n')
#분석에 필요한 열만 추출하여 새 df 생성


#- 3개 독립변수 루보 중 단순회귀분석에 사용할 변수 선택: weight
###- 종속 변수 Y인 "연비(mpg)"와 다른 변수 간의 선형관계를 그래프(산점도)로 확인

# Matplotlib으로 산점도 그리기: df.plot(kind=, x=,y=,''')
ndf.plot(kind='scatter', x='weight', y='mpg',  c='coral', s=10, figsize=(10, 5))
plt.show()
plt.close()

# seaborn으로 산점도 그리기: sns.regplot(x=,y=, data=, ax=)
fig = plt.figure(figsize=(10, 5)) # fig 크기 설정
ax1 = fig.add_subplot(1, 2, 1) # fig 1행 2개로 분할(ax 설정)
ax2 = fig.add_subplot(1, 2, 2)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1)         # default:  회귀선 표시
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax2, fit_reg=False)  #회귀선 미표시
plt.show()
plt.close()

# seaborn 조인트 그래프 - 산점도, 히스토그램: sns.jointplot(x=,y=,kind=추가옵션, data=)
# 산점도이되, 두 변수의 히스토그램이 각 축에 별도로 표시
sns.jointplot(x='weight', y='mpg', data=ndf)              # 회귀선 없음
sns.jointplot(x='weight', y='mpg', kind='reg', data=ndf)  # 회귀선 표시: kind='reg'
#회귀선 표시하는 경우 각 축의 히스토그램과, 산점도 모두에 회귀선 표시됨
plt.show()
plt.close()

# seaborn pariplot으로 두 변수 간의 모든 경우의 수 그리기: sns.pairplot(df)
# df의 열을 두개씩 짝지을 수 있는 모든 경우에 대하여 두 변수간 산점도 나타냄
# 앞의 코드들과 달리, 한번에 모든 변수 간 경우 확인 가능!
# (자기 자신과의 관계만 히스토그램)
sns.pairplot(ndf)  
plt.show()
plt.close()
#mpg를 Y로 두는 경우 확인하고 싶으므로, 모든 그림 중 y축이 mpg인 첫번째 줄의 경우를 확인 



'''
Step 4: 데이터셋 구분 - 훈련용(train data)/ 검증용(test data)
'''

#위의 코드 실행 시 mpg와 선형관계 갖는 horsepower, weight열을 x로 고려
#?? cylinder는 어떤 경우로 분류되는지

# 속성(변수) 선택
X=ndf[['weight']]  #독립 변수 X: dataframe으로 전달?
y=ndf['mpg']       #종속 변수 Y

# 두 변수간 회귀방정식 찾기

# train data 와 test data로 구분(7:3 비율)
# 이 부분 코드는 그냥 익히기 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,               #독립 변수 
                                                    y,               #종속 변수
                                                    test_size=0.3,   #검증 30%--> 훈련 70%
                                                    random_state=10) #랜덤 추출 값 

print('train data 개수: ', len(X_train))
print('test data 개수: ', len(X_test))


'''
Step 5: 단순회귀분석 모형 - sklearn 사용(모형 학습 및 검증) 
'''

# sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모형 객체 생성, lr에 저장
lr = LinearRegression()   

# train data를 가지고 모형 학습: lr. fit(x_train,y_train)
lr.fit(X_train, y_train)
# 모형 객체에 훈련 데이터 전달--> 모형이 학습을 통해 회귀방정식 계수 a,b 찾아냄

# 학습을 마친 모형에 test data를 적용하여 결정계수(R-제곱) 계산: lr.scor(x_test, y_test)
r_square = lr.score(X_test, y_test)
# 모형의 예측 능력 평가
#결정계수값이 클수록 모형의 예측능력 좋음! 이부분 이론적 내용 간단히 알아보기
print(r_square)
print('\n')


#회귀선의 관계식(회귀방정식)의 계수 확인 가능(a,b 모두 모형 lr객체의 속성)
# 회귀식의 기울기: lr.coef_ 
print('기울기 a: ', lr.coef_)
print('\n')

# 회귀식의 y절편: lr.intercept_
print('y절편 b', lr.intercept_)
print('\n')


#모형이 예측한 값과 실제 값 비교 : 에측값y_hat= lr.predict(X)
# 모형에 '전체 X' 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교 
y_hat = lr.predict(X)

# y_hat과 y를 같은 화면에 분포도를 그려서 비교: sns.displot() 
plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y, label="y")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
# 한 평면에 두개의 그래프 그리는 경우: 두번째 그래프의 ax=첫번째 그래프  로 옵션 추가
plt.legend()
plt.show()

# 실제 값: 왼쪽 편향, 예측 값: 오른쪽 편향
# 선형관계 있으나, 오파 줄여야 함
# 앞의 산점도: 곡선의 형태--> 비선형 회귀분석 필요
