# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 07:13:10 2022

@author: user
"""

import folium

seoul_map = folium.Map(location=[37.55,126.98], zoom_star=12)
seoul_map.save('./seoul.html')