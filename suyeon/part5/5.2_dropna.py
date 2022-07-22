# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# for 반복문으로 각 열의 NaN 개수 계산하기
missing_df = df.isnull() #NaN이면 True인 원본과 크기 동일한 df 반환
for col in missing_df.columns: #missing df의 column 리스트에 대해 반복
    missing_count = missing_df[col].value_counts()    # 각 열의 NaN 개수 파악
    #해당 열이 유효한 값(missing df의 유효 값, 즉 원본 df의 NaN값)이면 1 반환??

    try: 
        print(col, ': ', missing_count[True])   # NaN 값이 있으면 개수를 출력
       #??
    except:
        print(col, ': ', 0)                     # NaN 값이 없으면 0개 출력
        

        
# NaN 값이 500개 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)
df_thresh = df.dropna(axis=1, thresh=500)  #axis: 행, 열 설정, thresh: 삭제 기준 되는 NaN 개수
print(df_thresh.columns)

# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
df_age = df.dropna(subset=['age'], how='any', axis=0)  
#subset=['']: dropna 적용 범위 한정
#how='any': NaN이 하나라도 있는 모든 행 삭제
#axis=0: 행 삭제
#남은 행, 즉 유효 나이값 있는 행만 저장
print(len(df_age)) # 유효 나이값 있는 행 개수

