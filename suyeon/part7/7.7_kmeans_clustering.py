# -*- coding: utf-8 -*-
#4. 군집 Clustering 분석
# 데이터셋의 관측값이 갖고 있는 여러 속성을 분석하여 
#서로 비슷한 특징을 갖는 관측값끼리 같은 클러스터(군집)으로 묶는 알고리즘

#각 클러스터끼리 서로 완전히 구분--> 어느 클러스터에도 속하지 않는 관측값 존재 가능
                                  #특이 데이터(이상값, 중복값) 찾는데 활용 가능
#비지도 학습 유형(관측값을 몇개 집단으로 구분한다는 점이 분류classification 알고리즘과 유사)
#차이점: 정답이 없는 상태에서 데이터 자체의 유사성만을 기준으로 판단

#구매 패턴 분석 등 소비자 행동 특성 그룹화 시 사용
# 유사 특성 갖는 집단 구분 시 새 소비자의 구매 패턴이나 행동 예측 가능

#k-means 알고리즘, DBSCAN 알고리즘 등

#4-1. k-means
# 데이터 간의 유사성 측정 기준: 각 클러스터의 중심까지의 거리
# 벡터 공간의 어떤 데이터에 대해, k개의 클러스터 중 중심까지 거리가 가장 가까운 클러스터로 할당
# 각 클러스터간 일정 거리 이상 떨어지게 설정
# k가 클수록 모형 성능 개성(단 너무 커지면 분류/분석의 효과 감소)

### 기본 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt


'''
[Step 1] 데이터 준비
'''

# Wholesale customers 데이터셋 가져오기 (출처: UCI ML Repository) (도매업 고객)
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path, header=0)


'''
[Step 2] 데이터 탐색
'''

# 데이터 살펴보기
print(df.head())   
print('\n')

# 데이터 자료형 확인
print(df.info())  #모두 정수형
print('\n')

# 데이터 통계 요약정보 확인
print(df.describe())
print('\n')


'''
[Step 3] 데이터 전처리
'''

# 분석에 사용할 속성을 선택
X = df.iloc[:, :] 
# df 전체를 모형의 학습 데이터로 사용
# 비지도 학습 모형: 모든 속성을 설명 변수로 지정, 예측 변수Y 지정할 필요 없음
print(X[:5])
print('\n')

# 설명 변수 데이터를 정규화(데이터값의 상대적 크기 차에서 오는 오류 제거)
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)
#리턴: X_newndarray array of shape (n_samples, n_features_new) : Transformed array.
#https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

print(X[:5])
print('\n')


'''
[Step 4] k-means 군집 모형 - sklearn 사용 (모형 학습 및 검증)
'''

# sklearn 라이브러리에서 cluster 군집 모형 가져오기
from sklearn import cluster

# 모형 객체 생성 : cluster.Kmeans()
kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)
#n_clusters=5: 클러스터 개수 지정
#init: method for initialization:‘k-means++’ : selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. 
#n_init: Number of time the k-means algorithm will be run with different centroid seeds.
#https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

# 모형 학습
kmeans.fit(X) #모형이 스스로 학습해 설정한 클러스터 개수 만큼 데이터 구분   

# 예측 (군집) 
cluster_label = kmeans.labels_ #모형이 구분한 클러스터 값 저장
print(cluster_label) #각 데이터에 대해, 0~4 범위의 클러스터 확인
print('\n')

# 예측 결과를 데이터프레임에 추가(새로운 열)
df['Cluster'] = cluster_label
print(df.head())   
print('\n')


# 그래프 표현
# 모형이 8개의 변수(속성, 열)이용해 각 관측값을 5개의 클러스터로 구분
# 8개 변수 한번에 못나타내므로 2개 변수 임의로 선택, 관측값 분포 보기

# 모형의 예측값이 매 시행마다 달라지므로 그래프 모양도 달라짐!

# 그래프로 표현 - 시각화: df.plot(kind='scatter',): 산점도로 표현
df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', 
        colorbar=False, figsize=(10, 10))
        #c='Cluster': 점의 색으로 표시되는 속성; 모델의 예측값
df.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', 
        colorbar=True, figsize=(10, 10))

plt.show()
plt.close()

# 그래프 표현 - 큰 값으로 구성된 클러스터(0, 4)를 제외 
# 값이 몰려 있는 구간을 자세하게 분석
mask = (df['Cluster'] == 0) | (df['Cluster'] == 4) 
ndf = df[~mask] #클러스터 1,2,3만 따로 저장

#산점도
ndf.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', 
        colorbar=False, figsize=(10, 10))
ndf.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', 
        colorbar=True, figsize=(10, 10))
plt.show()
plt.close()

# 지나치게 큰 값 제외한다는게 이상값 같은 걸 줄인다는 의미임?
