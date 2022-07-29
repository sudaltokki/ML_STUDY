# -*- coding: utf-8 -*-

#3-3. Decision Tree 의사결정 나무
# tree 구조 사용, 각 node에는 분석 대상의 속성(설명변수)이 위치
# 각 분기점에서 해당 속성이 갖는 값으로 새 branch 생성
            # 최적 속성 선택 시, 해당 속성 기준 분류한 값들이 구분되는 정도 측정
            # Entropy(다른 종류의 값들이 섞여 있는 정도)가 낮을수록 분류가 잘 된것 (일정수준 이하로 낮아질때까지 과정 반복)


# 기본 라이브러리 불러오기
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np

'''
[Step 1] 데이터 준비/ 기본 설정
'''

# Breast Cancer 데이터셋 가져오기 (출처: UCI ML Repository) (암세포 진단, p324 설명 간단 참고)
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)

# 열 이름 지정
df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
              'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']

#  IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns', 15)


'''
[Step 2] 데이터 탐색
'''

# 데이터 살펴보기
print(df.head())
print('\n')

# 데이터 자료형 확인
print(df.info()) #bare nuclei열 제외 모두 int이므로, 이 열만 숫자형으로 변환하면 됨
print('\n')

# 데이터 통계 요약정보 확인
print(df.describe())
print('\n')

# bare_nuclei 열의 자료형 변경 (문자열 ->숫자) 
# bare_nuclei 열의 고유값 확인
print(df['bare_nuclei'].unique()) #'?'섞여 있음 
print('\n')

df['bare_nuclei'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)   # 누락데이터 행을 삭제
#699개 중 16개 삭제되어 683개 관측값 남음
df['bare_nuclei'] = df['bare_nuclei'].astype('int')       # 문자열을 정수형으로 변환

print(df.describe())                                      # 데이터 통계 요약정보 확인
print('\n')


'''
[Step 3] 데이터셋 구분 - 훈련용(train data)/ 검증용(test data)
'''

# 속성(변수) 선택
X = df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
        'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]  # 설명 변수 X: df 형으로 전달
y = df['class']  # 예측 변수 Y

# 설명 변수 데이터를 정규화
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data 와 test data로 구분(7:3 비율)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=10)

print('train data 개수: ', X_train.shape) #(데이터 개수(행개수), 속성 개수(열 개수))
print('test data 개수: ', X_test.shape)
print('\n')


'''
[Step 4] Decision Tree 분류 모형 - sklearn 사용 (모형 학습 및 검증)
'''

# sklearn 라이브러리에서 Decision Tree 분류 모형 가져오기(line 12에서 수행)

# 모형 객체 생성 (criterion='entropy' 적용): tree.DecisionTreeClassifier(criterion=, max_depth=)
tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)
# criterion='entropy': 각 분기점에서 최적 속성 찾기 위한 분류 정도 평가 기준
# max_depth=5: 5단계까지 가지 확장 가능
    #레벨 늘어날수록 훈련 데이터에 대한 예측 정확해지지만, 
    #실제 데이터에 대한 예측 능력은 떨어짐

# train data를 가지고 모형 학습
tree_model.fit(X_train, y_train)

# test data를 가지고 y_hat을 예측 (분류)
y_hat = tree_model.predict(X_test)      # 2: benign(양성), 4: malignant(악성)

#실제 값y_test와 예측 값y_hat 비교
print(y_hat[0:10])
print(y_test.values[0:10])
print('\n') #모두 일치

#모형 평가 지표 계산
# 모형 성능 평가 - Confusion Matrix 계산
tree_matrix = metrics.confusion_matrix(y_test, y_hat) #[[TN,FP],[FN,TP]]
print(tree_matrix)
print('\n')

# 모형 성능 평가 - 평가지표 계산
tree_report = metrics.classification_report(y_test, y_hat)
#악성 종양 예측 정확도와 양성 종양 예측 정확도에 큰 차이 없음(표본평균 weighted avg(표본 갯수 고려): 0.97)
# https://datascienceschool.net/03%20machine%20learning/09.04%20%EB%B6%84%EB%A5%98%20%EC%84%B1%EB%8A%A5%ED%8F%89%EA%B0%80.html
print(tree_report)
