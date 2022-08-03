# -*- coding: utf-8 -*-

import matplotlib

# Matplotlib 라이브러리에서 사용할 수 있는 색상의 종류 확인
# 컬러 정보를 담을 빈 딕셔너리 생성
colors = {}

# 컬러 이름과 헥사코드 확인하여 딕셔너리에 입력
for name, hex in matplotlib.colors.cnames.items():
    colors[name] = hex
    
# 딕셔너리 출력
print(colors)