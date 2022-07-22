# -*- coding: utf-8 -*-
#4-38. 지도에 마커 표시하기
#Marker() :마커 함수에 위도, 경도 정보 전달 시 마커 위치 표시 가능
#popup= :옵션추가시 마커 클릭 시 팝업창에 표시되는 텍스트 설정 가능 

# 라이브러리 불러오기
import pandas as pd
import folium

# 대학교 리스트를 데이터프레임으로 변환
df = pd.read_excel('./서울지역 대학교 위치.xlsx', engine= 'openpyxl')

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)

# 대학교 위치정보를 Marker로 표시
for name, lat, lng in zip(df.index, df.위도, df.경도): 
    #파이썬 내장 zip(): zip() 함수를 활용하면 여러 그룹의 데이터를 루프를 한 번만 돌면서 처리. 가변 인자를 받기 때문에 2개 이상의 인자를 넘겨서 병렬 처리.
    #https://www.daleseo.com/python-zip/
    
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)
    #add_to() 함수를 이용해 미리 만들어둔 folium 변수에 내용을 추가
    #https://dudgns7675.tistory.com/6

# 지도를 HTML 파일로 저장하기
seoul_map.save('./seoul_colleges.html')
#??왜 팝업창에 숫자 나오는지