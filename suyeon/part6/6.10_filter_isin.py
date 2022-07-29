# -*- coding: utf-8 -*-
#3-2. isin() 메소드 활용 
#df의 열에 isin() 적용시, 특정 값을 가진 행들만 따로 추출

#isin()메소드를 활용한 필터링: df의 열객체.isin(추출값의 리스트)
#line 26

# 라이브러리 불러오기
import seaborn as sns
import pandas as pd

# titanic 데이터셋 로딩
titanic = sns.load_dataset('titanic')

# IPyhton 디스플레이 설정 변경 - 출력할 최대 열의 개수
pd.set_option('display.max_columns', 10)  
# https://www.codetd.com/ko/article/13793718#:~:text=pd.set_option%20%28%27expand_frame_repr%27%2CTrue%29%3A%20True%EB%8A%94%20%EC%97%B4%EC%9D%B4%20%EC%83%88%20%EC%A4%84%EC%97%90%20%ED%91%9C%EC%8B%9C%EB%90%A0%20%EC%88%98,%ED%97%88%EC%9A%A9%EB%90%98%EC%A7%80%20%EC%95%8A%EC%8A%B5%EB%8B%88%EB%8B%A4.%20pd.set_option%20%28%27display.max_columns%27%2C%20None%29%3A%20%EB%AA%A8%EB%93%A0%20%EC%97%B4%EC%9D%84%20%ED%91%9C%EC%8B%9C%ED%95%A9%EB%8B%88%EB%8B%A4.

    
# 함께 탑승한 형제 또는 배우자의 수가 3, 4, 5인 승객만 따로 추출 - 불린 인덱싱
mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5
df_boolean = titanic[mask3 | mask4 | mask5]
print(df_boolean.head())
print('\n')

# isin() 메서드 활용하여 동일한 조건으로 추출
isin_filter = titanic['sibsp'].isin([3, 4, 5])
#df열.isin([]): 인자 리스트 안의 값이 존재하는 행은 참을 반환, 값이 없으면 거짓을 반환--> 불린 시리즈 반환

df_isin = titanic[isin_filter] #불린 전달하여 참인 행만 df_isin에 저장

print(df_isin.head())
