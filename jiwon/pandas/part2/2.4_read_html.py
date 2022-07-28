# -*- coding: utf-8 -*-

import pandas as pd

'''
read_html() 함수로 HTML 웹 페이지에 있는 <table> 태그에서 표 형식의 데이터를 
모두 찾아서 데이터프레임으로 변환한다.
표 데이터들은 가각의 별도의 데이터프레임으로 변환되기 때문에 여러 개의 데이터프레임을
원소로 갖는 리스트가 반환된다.

read_html() 함수를 이용해 웹 페이지의 표 정보를 파싱(parsing)하려면 HTMl 웹 페이지의
주소(URL)을 따옴표 안에 입력한다.

예제에서는 실제 웹 페이지 주소 대신 HTML 파일의 경로를 사용한다.
'''

# HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url = './sample.html'

# HTML 웹 페이지의 표(table)를 가져와서 데이터프레임으로 변환
tables = pd.read_html(url)

# 표(table) 개수 확인
print(len(tables))
print('\n')

# tables 리스트의 원소를 iteration하면서 각각 화면 출력
for i in range(len(tables)) :
    print('tables[%s]' % i)
    print(tables[i])
    print('\n')
    
# 두 번째 데이터프레임을 선택해 변수 df에 저장
df = tables[1]

# 'name'열을 인덱스로 지정
df.set_index(['name'], inplace=True)
print(df)