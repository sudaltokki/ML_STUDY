# -*- coding: utf-8 -*-
#3. Folium Libarary-지도 활용
#4-36. 지도 만들기: folium.Map()
#생성된 지도: zoom, scroll 모두  가능한 고정되지 않은 화면
#웹기반 지도 생성--> 웹기만 IDE에서 실행하거나, 스파이더에서 실행 후 html파일로 저장하고 웹브라우저에서 파일 열기

# 라이브러리 불러오기
import folium

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], zoom_start=12)
#location=[위도, 경도]: 지도 보여주는 기준점, zoom_start=화면 확대 비율 조절

# 지도를 HTML 파일로 저장하기: folium객체.save()
seoul_map.save('./seoul.html')