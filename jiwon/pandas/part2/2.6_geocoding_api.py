# -*- coding: utf-8 -*-

'''
인터넷 서비스 업체에서 제공하는 API를 통해서 수집한 데이터를 판다스 자료구조로 변환하는 방법
대부분의 API는 판다스에서 쉽게 읽어올 수 있는 파일 형식(csv, json, xml, ...)들을 지원

구글 지오코딩은 장소 이름 또는 주소를 입력하면 위도와 경도 좌표 정보를 변환해주는 서비스
지오코딩을 사용하기 위해서는 API 키 발급, googlemaps 라이브러리 설치가 필요

구글 지오코딩 API를 호출했을 때 반환하는 결과의 예시는 다음과 같다.
{'location': {'lat': 35.1586975, 'lng': 129.1603842},
 'location_type': 'APPROXIMATE',
 'viewport': {'northeast' :{'lat': 35.1678193, 'lng': 129.1763916}, 
              'southwest': {'lat': 35.1495747, 'lng': 129.1443768}}
}

location을 키로 하는 데이터에서 lat과 lng가 나타내는 값은 위도와 경도이다.
'''

import googlemaps
import pandas as pd

my_key = 'AIzaSyDCbManBKv0i5P2Md3nz2nSlbCCiuQqEv0'

# 구글맵스 객체 생성하기
maps = googlemaps.Client(key=my_key)

lat = [] # 위도
lng = [] # 경도

# 장소 리스트
places = ["서울시청", "국립국악원", "해운대해수욕장"]

i = 0
for place in places:
    i = i + 1
    try:
        print(i, place)
        # 지오코딩 API 결과값 호출하여 geo_location 변수에 저장
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])

    except:
        lat.append('')
        lng.append('')
        print(i)
        
# 데이터프레임으로 변환
df = pd.DataFrame({'위도':lat, '경도':lng}, index=places)
print('\n')
print(df)

'''
머신러닝에 유용한 데이터셋 소스

데이터분석과 머신러닝을 공부할 떄 데이터셋을 제공하는 곳을 알아두면 많은 도움이 된다.
1. 사이킷런, 시본 등 파이썬 라이브러리 제공 데이터셋
2. 캐글
3. UCI 머신러닝 저장소
4. 공공데이터
    (해외) WorldBank, WTO 등 국제기구
    (국내) 공공데이터 포탈, 국가통계포털 
'''