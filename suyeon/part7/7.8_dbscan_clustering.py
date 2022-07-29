# -*- coding: utf-8 -*-
#4-2. DBSCAN Density -Based Spatial Clustering of Applications with Noise
# 해당 데이터가 위치하고 있는 공간 밀집도를 기준으로 클러스터 구분
# core point: 자기를 중심으로 반지름 R의 공간에 최소 M개의 포인트가 존재하는 점
# border point: 코어 포인트는 아니지만 R 안에 다른 코어 포인트가 있는 경우
# noise(outlier): 코어포인트도 아니고 보더포인트에도 속하지 않는 점, 어느 클러스터에도 속하지 않는 점
#하나의 클러스터는 R안에 서로 위치하는 모든 코어 포인트를 포함(서로 밀접한 데이터가 하나의 클러스터)

### 기본 라이브러리 불러오기
import pandas as pd
import folium


'''
[Step 1] 데이터 준비/ 기본 설정
'''

# 서울시내 중학교 진학률 데이터셋 (출처: 교육???)
file_path = './2016_middle_shcool_graduates_report.xlsx' #파이썬 코드와 같은 폴더에 위치시키기
df = pd.read_excel(file_path, engine='openpyxl', header=0)

# IPython Console 디스플레이 옵션 설정하기
pd.set_option('display.width', None)        # 출력화면의 너비
pd.set_option('display.max_rows', 100)      # 출력할 행의 개수 한도
pd.set_option('display.max_columns', 10)    # 출력할 열의 개수 한도
pd.set_option('display.max_colwidth', 20)   # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 열 이름 배열을 출력
print(df.columns.values)   
print('\n')


'''
[Step 2] 데이터 탐색
'''

# 데이터 살펴보기
print(df.head())   
print('\n')

# 데이터 자료형 확인
print(df.info())  #20개 열(속성), 415개 행(데이터 수)
print('\n')

# 데이터 통계 요약정보 확인
print(df.describe())
print('\n')

# 지도에 위치 표시
    # 지도 시작점 등 설정하여 지도 객체 생성
mschool_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)



# 중학교 위치정보를 CircleMarker로 표시
    #각 중학교 위치인 '위도'열, '경도' 열을 folium.circlemarker()에 전달
    #각 위치가 지도에 원형 마커로 표시됨
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius=5,              # 원의 반지름
                        color='brown',         # 원의 둘레 색상
                        fill=True,
                        fill_color='coral',    # 원을 채우는 색
                        fill_opacity=0.7,      # 투명도    
                        popup=name #원형 마커 클릭 시 학교명이 팝업 표시
    ).add_to(mschool_map)


# 지도를 html 파일로 저장하기-->스파이더에서 확인하기 위함
mschool_map.save('./seoul_mschool_location.html')


'''
[Step 3] 데이터 전처리
'''

# 원핫인코딩(더미 변수)
# 열 데이터 중 모형이 인식할 수 없는 문자열 데이터를 더미 변수로 변환
from sklearn import preprocessing    

label_encoder = preprocessing.LabelEncoder()     # label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder()   # one hot encoder 생성??

onehot_location = label_encoder.fit_transform(df['지역']) #원핫인코딩으로 변환
onehot_code = label_encoder.fit_transform(df['코드'])  #0~데이터종류-1 까지의 정수형 데이터 종류로 변환?
onehot_type = label_encoder.fit_transform(df['유형'])
onehot_day = label_encoder.fit_transform(df['주야'])

df['location'] = onehot_location #df에 추가
df['code'] = onehot_code
df['type'] = onehot_type
df['day'] = onehot_day

print(df.head())   
print('\n')


'''
[Step 4] DBSCAN 군집 모형 - sklearn 사용(모형 학습 및 검증)
'''

# sklearn 라이브러리에서 cluster 군집 모형 가져오기 
from sklearn import cluster

# 분석에 사용할 속성을 선택 (과학고, 외고국제고, 자사고 진학률)
columns_list = [9, 10, 13]
X = df.iloc[:, columns_list] #모든 행(관측값)에 대해 , 위의 3개 열만 추출
print(X[:5])
print('\n')

# 설명 변수 데이터를 정규화
X = preprocessing.StandardScaler().fit(X).transform(X)

# DBSCAN 모형 객체 생성: cluster.DBSCAN
dbm = cluster.DBSCAN(eps=0.2, min_samples=5)
#eps: 밀도 계산의 기준이 되는 반지름 R
#min_samples: 최소 포인트 개수 M


# 모형 학습
dbm.fit(X)   #모형이 데이터를 여러 클러스터로 구분
 
# 예측 (군집) 
cluster_label = dbm.labels_   
print(cluster_label) #라벨 값 종류 5개: -1,0,1,2,3 
                    #클러스터 값 종류 4개: 0,1,2,3 
                    #( -1은 noise를 나타냄, 클러스터 종류서 제외)
print('\n')

# 예측 결과를 데이터프레임에 새 열로 추가
df['Cluster'] = cluster_label
print(df.head())   
print('\n')

# 클러스터 값으로 그룹화하고, 그룹별로 내용 출력 (첫 5행만 출력)
#새 df의 열에는 앞서 선택한 3개의 속성과  cluster에 대해 추가된 ???
grouped_cols = [0, 1, 3] + columns_list #???

#'Cluster'열 기준 df를 그룹 객체로 변환
grouped = df.groupby('Cluster') 


for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))    
    print(group.iloc[:, grouped_cols].head()) #각 그룹별로, 특정 열 속성만 출력
    print('\n')
#p 348 데이터 해석 확인


# 그래프로 표현 - 시각화
#Noise의 경우 회색 설정, 색을 딕셔너리{:,:}로 전달
colors = {-1:'gray', 0:'coral', 1:'blue', 2:'green', 3:'red', 4:'purple', 
          5:'orange', 6:'brown', 7:'brick', 8:'yellow', 9:'magenta', 10:'cyan', 11:'tan'}

cluster_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster):  
    folium.CircleMarker([lat, lng],
                        radius=5,                   # 원의 반지름
                        color=colors[clus],         # 원의 둘레 색상 color
                        fill=True,
                        fill_color=colors[clus],    # 원을 채우는 색 fill_color
                        fill_opacity=0.7,           # 투명도    
                        popup=name
    ).add_to(cluster_map)

# 지도를 html 파일로 저장하기
cluster_map.save('./seoul_mschool_cluster.html')




# X2) 데이터셋에 대하여 위의 과정을 반복(과학고, 외고국제고, 자사고 진학률 + 유형)
#앞에서 선택한 속성에 학교 설립 유형을 추가하여 분석
columns_list2 = [9, 10, 13, 22]
X2 = df.iloc[:, columns_list2]
print(X2[:5])
print('\n')


X2 = preprocessing.StandardScaler().fit(X2).transform(X2)#정규화
dbm2 = cluster.DBSCAN(eps=0.2, min_samples=5) #객체 생성
dbm2.fit(X2)  #훈련
df['Cluster2'] = dbm2.labels_ #각 관측값 행에 대한 클러스터 저장   

grouped2_cols = [0, 1, 3] + columns_list2
grouped2 = df.groupby('Cluster2') #cluster 열 종류에 따라 그룹화
for key, group in grouped2: #그룹 별 개수, 5개행 등 출력
    print('* key :', key)
    print('* number :', len(group))    
    print(group.iloc[:, grouped2_cols].head())
    print('\n')

#지도 객체 생성
cluster2_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)
#지도에 원형 점 추가
for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster2):  
    folium.CircleMarker([lat, lng],
                        radius=5,                   # 원의 반지름
                        color=colors[clus],         # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus],    # 원을 채우는 색
                        fill_opacity=0.7,           # 투명도    
                        popup=name
    ).add_to(cluster2_map)

# 지도를 html 파일로 저장하기
cluster2_map.save('./seoul_mschool_cluster2.html')
#속성 추가-->클러스터 종류 늘어남(분류 유형 늘어남)


#속성을 2개로 줄여서 예측
# X3) 데이터셋에 대하여 위의 과정을 반복(과학고, 외고_국제고만 사용)
columns_list3 = [9, 10]
X3 = df.iloc[:, columns_list3]
print(X3[:5])
print('\n')

X3 = preprocessing.StandardScaler().fit(X3).transform(X3)
dbm3 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm3.fit(X3)  
df['Cluster3'] = dbm3.labels_   

grouped3_cols = [0, 1, 3] + columns_list3
grouped3 = df.groupby('Cluster3')
for key, group in grouped3:
    print('* key :', key)
    print('* number :', len(group))    
    print(group.iloc[:, grouped3_cols].head())
    print('\n')

cluster3_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster3):  
    folium.CircleMarker([lat, lng],
                        radius=5,                   # 원의 반지름
                        color=colors[clus],         # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus],    # 원을 채우는 색
                        fill_opacity=0.7,           # 투명도    
                        popup=name
    ).add_to(cluster3_map)

# 지도를 html 파일로 저장하기
cluster3_map.save('./seoul_mschool_cluster3.html')
# 첫번째 케이스보다는 클러스터 다양, 두번째 케이스보다는 클러스터 적음
