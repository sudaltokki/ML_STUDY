# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:47:57 2022

@author: user
"""

#try 부분을 잘 못하는데 이유를 모르겠다
import googlemaps
import pandas as pd

my_key = "-"

maps = googlemaps.Client(key=my_key)

lat = []
lng = []

places = ["서울시청", "국립국악원", "헤운대해수욕장"]

i=0
for place in places:
    i=i+1
    try:
        print(i,place)
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])

    except:
        lat.append('')
        lng.append('')
        print(i)

df = pd.DataFrame({'위도':lat, '경도':lng}, index = places)
print('\n')
print(df)