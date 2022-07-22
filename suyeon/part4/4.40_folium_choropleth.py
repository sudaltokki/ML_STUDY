# -*- coding: utf-8 -*-
#4-40. 지도 영역에 단계구분도(Choropleth Map) 표시하기
#folium.Choropleth()
#행정구역과 같이 지도 상의 어떤 경계에 둘러싸인 영역에 색을 칠하거나 음영 등으로 정보를 나타내는 시각화 방법
#전달하려는 정보의 값의 커지면 영역의 색이나 음영이 진해짐
#지도 종류 달라지더라도 Map()통해 지도 객체는 생성해야함



# 라이브러리 불러오기
import pandas as pd
import folium
import json

# 경기도 인구변화 데이터를 불러와서 데이터프레임으로 변환
#경기도 인구변화 데이터
file_path = './경기도인구데이터.xlsx'
df = pd.read_excel(file_path, index_col='구분', engine= 'openpyxl')  
df.columns = df.columns.map(str) #column 이름을 string으로 변환

# 경기도 시군구 경계 정보를 가진 geo-json 파일 불러오기
#경기도 행정구역 경계 데이터
geo_path = './경기도행정구역경계.json'
try:
    geo_data = json.load(open(geo_path, encoding='utf-8'))
except: #에러 발생 시 아래 시행
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))

# 경기도 지도 객체 만들기
g_map = folium.Map(location=[37.5502,126.982], 
                   tiles='Stamen Terrain', zoom_start=9)

# 출력할 연도 선택 (2007 ~ 2017년 중에서 선택)
year = '2017'  

# Choropleth 클래스로 단계구분도 표시하기
folium.Choropleth(geo_data=geo_data,    # 지도 경계 
                 data = df[year],      # 표시하려는 데이터 
                 columns = [df.index, df[year]],  # 열 지정
                 fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3, #opacity: 불투명도
                 threshold_scale=[10000, 100000, 300000, 500000, 700000], #? 축적  (https://yssa.tistory.com/entry/Python-%ED%8F%B4%EB%A6%AC%EC%97%84Folium-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%ACLibrary)               
                 key_on='feature.properties.name',
                 ).add_to(g_map)

"""folium.Choropleth(
    geo_data = "지도 데이터 파일 경로 (.geojson, geopandas.DataFrame)"
    data = "시각화 하고자 하는 데이터파일. (pandas.DataFrame)"
    columns = (지도 데이터와 매핑할 값, 시각화 하고자하는 변수),
    key_on = "feature.데이터 파일과 매핑할 값",
    fill_color = "시각화에 쓰일 색상",
    legend_name = "칼라 범주 이름",
).add_to(m)"""
    
    #https://dailyheumsi.tistory.com/m/144?category=854906

# 지도를 HTML 파일로 저장하기
g_map.save('./gyonggi_population_' + year + '.html')