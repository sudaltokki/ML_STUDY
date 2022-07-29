# -*- coding: utf-8 -*-
# 3. 분류 classification 알고리즘
# 예측하려는 대상의 속성(설명 변수)을 입력 받고, 목표 변수가 갖고 있는 카테고리(범주형) 값 중에서 어느 한 값으로 분류하여 예측
# 지도 학습(훈련 데이터에 목표 변수 값 0/1을 함께 입력)
# 종류: KNN,SVM,Decision Tree,Logistic Regression 등
# 고객 분류, 질병 진단, 스팸 메일 필터링, 음성 인식 등 목표 변수가 카테고리 값을 갖는 경우 사용



#3-1. KNM:k-Nearest- Neighbors  k개의 가까운 이웃
# 새 관측값이 주어지면, 기존 데이터 중에서 가장 속성이 비슷한 k개의 이웃을 찾은 후,
#가까운 이웃들이 갖고 있는 목표값과 같은 값으로 분류하여 예측
#k 값에 따라 예측의 정확도가 달라지므로 적절 k 찾는 것이 중요


#탑승객의 생존 여부 예측 모형 만들기
### 기본 라이브러리 불러오기
import pandas as pd
import seaborn as sns

'''
[Step 1] 데이터 준비 - Seaborn에서 제공하는 titanic 데이터셋 가져오기
'''

# load_dataset 함수를 사용하여 데이터프레임으로 변환
df = sns.load_dataset('titanic')

# 데이터 살펴보기
print(df.head())   
print('\n')

#  IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns', 15)
print(df.head())   
print('\n')


'''
[Step 2] 데이터 탐색
'''

# 데이터 자료형 확인
print(df.info())  
print('\n')

#아래의 열별로 적절히 선택하는 데이터 처리 방식 확인

# NaN값이 많은 deck 열을 삭제, embarked와 내용이 겹치는 embark_town 열을 삭제
rdf = df.drop(['deck', 'embark_town'], axis=1)  # df.drop([],axis): 특정 열 삭제
print(rdf.columns.values) #남은 columns  확인
print('\n')

# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
# 즉 714 승객만 분석 대상
rdf = rdf.dropna(subset=['age'], how='any', axis=0)  #이 외에도 평균 나이로 치환하는 방법도 가능
print(len(rdf))
print('\n')

# embarked 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()   
# .value_count: 데이터의 고유값별로 몇개씩 들어있는지 알고 싶을때 유용
#   dropna=True: 부울. NaN (dropna = False) 개수를 포함하거나NaN (dropna = True) 개수를 제외
# https://www.delftstack.com/ko/api/python-pandas/pandas-series-series.value_counts-function/   https://jaaamj.tistory.com/112#:~:text=%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98%20%EA%B3%A0%EC%9C%A0%EA%B0%92%EB%B3%84%EB%A1%9C%20%EB%AA%87%EA%B0%9C%EC%94%A9%20%EB%93%A4%EC%96%B4%EC%9E%88%EB%8A%94%EC%A7%80%20%EC%95%8C%EA%B3%A0%20%EC%8B%B6%EC%9D%84%EB%95%8C%20%EC%9C%A0%EC%9A%A9%ED%95%9C%20%ED%95%A8%EC%88%98%EC%9E%85%EB%8B%88%EB%8B%A4.,%EC%A0%95%EB%A0%AC%EC%9D%84%20%ED%95%98%EA%B3%A0%20%EC%8B%B6%EB%8B%A4%EB%A9%B4%20ascending%3DTrue%20%EC%98%B5%EC%85%98%EC%9D%84%20%EC%A7%80%EC%A0%95%ED%95%B4%20%EC%A3%BC%EB%A9%B4%20%EB%90%A9%EB%8B%88%EB%8B%A4.    

# .idxmax(): 행에서 최대 값의 색인을 반환합니다. 또는 열/ 문자열 인덱스의 경우 제일 첫 글자 반환
#https://www.delftstack.com/ko/api/python-pandas/pandas-dataframe-dataframe.idxmax-function/
print(most_freq)
print('\n')

print(rdf.describe(include='all')) #embarked 열의 최빈값: s
print('\n')

rdf['embarked'].fillna(most_freq, inplace=True) #누락값 변환: .fillna( 바꾸는 값, inplace)



'''
[Step 3] 분석에 사용할 속성을 선택
'''

# 분석에 활용할 열(속성)을 선택 
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
#dataframe으로 전달
print(ndf.head())   
print('\n')

# 원핫인코딩 - 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변환
#             더미 변수를 만들고 이어붙임:  pd.get_dummies, pd. concat
onehot_sex = pd.get_dummies(ndf['sex']) 
#2개의 더미 변수 열이 만들어짐(male, female)
ndf = pd.concat([ndf, onehot_sex], axis=1) #pd.concat: 두 df를 이어 붙임

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town') 
#3개의 더미변수 열 생성
# prefix='town': 열 이름에 접두어 town 붙이기(town_C, town_Q, town_S)
ndf = pd.concat([ndf, onehot_embarked], axis=1)

ndf.drop(['sex', 'embarked'], axis=1, inplace=True) #기존 열 삭제
print(ndf.head())   
print('\n')


'''
[Step 4] 데이터셋 구분 - 훈련용(train data)/ 검증용(test data) (훈련/검증 데이터 분할)
'''

# 속성(변수) 선택
X=ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 
       'town_C', 'town_Q', 'town_S']]  #독립 변수 X: dataframe으로 전달
y=ndf['survived']                      #종속 변수 Y

# 설명 변수 데이터를 정규화(normalization)
# 각 설명변수 열이 갖는 데이터의 상대적 크기 차 없애기 위함
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10) 

print('train data 개수: ', X_train.shape) #(행 개수, 열 개수)
print('test data 개수: ', X_test.shape)


# 분류 모형의 예측력 평가 지표(p 316 각 지표 별 정의와 식 확인) 
# Confusion matrix, 정확도Precision, 재현율Recall,F1지표 F1-score
# f1-score: 정확도와 재현율의 조화 평균(균등 반영 가능)으로, 
# 값이 높을수록 분류 모형의 예측력이 좋음


'''
[Step 5] KNN 분류 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 KNN 분류 모형 가져오기
from sklearn.neighbors import KNeighborsClassifier

# 모형 객체 생성 (k=5로 설정)
knn = KNeighborsClassifier(n_neighbors=5)

# train data를 가지고 모형 학습
knn.fit(X_train, y_train)   

# test data를 가지고 y_hat을 예측 (분류) 
y_hat = knn.predict(X_test)

#예측값과 실제값을 비교
print(y_hat[0:10])
print(y_test.values[0:10])


# 모형의 예측 능력 평가
# 모형 성능 평가 - Confusion Matrix 계산: metrices.confusion_matrix(y_test,y_hat)
from sklearn import metrics 
knn_matrix = metrics.confusion_matrix(y_test, y_hat)  
#반환: [[TN,FP], [FN,TP]]
print(knn_matrix)

# 모형 성능 평가 - 평가지표 계산: metrices.classification_report(y_test, y_hat)
knn_report = metrics.classification_report(y_test, y_hat)    
# precision, recall, f1-score 출력        
print(knn_report)