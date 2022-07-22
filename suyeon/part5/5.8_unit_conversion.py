# -*- coding: utf-8 -*-
#3. 데이터 표준화 
# 여러곳에서 수집한 데이터는 단위 선택, 다른 형식, 대소문자, 약칭 등 서로 다른 표현법으로 동일 대상 표현
#따라서 데이터 포맷을 동일하게 변경-> 데이터 표준화

#3-1) 단위 환산
#5-8 단위 환산



# 라이브러리 불러오기
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 
print(df.head(3))    
print('\n')

# mpg(mile per gallon)를 kpl(kilometer per liter)로 변환 (mpg_to_kpl = 0.425)
#1마일에 대응하는 킬로미터 값/1갤런에 대응하는 리터값 = 0.425
mpg_to_kpl = 1.60934 / 3.78541
#1mpg=0.425 km/l

# mpg 열에 0.425를 곱한 결과를 새로운 열(kpl)에 추가
df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head(3))    
print('\n')

# kpl 열을 소수점 아래 둘째 자리에서 반올림한 값으로 다시 저장 : .round(n)
df['kpl'] = df['kpl'].round(2)
print(df.head(3))     