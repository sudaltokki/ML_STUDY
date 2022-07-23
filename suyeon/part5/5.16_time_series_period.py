# -*- coding: utf-8 -*-
#5-16. Timestamp를 Period로 변환
#to_period() : timestamp객체를 period객체로 변환
#freq 옵션에 기준이 되는 기간 설정

#line 19

# 라이브러리 불러오기
import pandas as pd

# 날짜 형식의 문자열로 구성되는 리스트 정의
dates = ['2019-01-01', '2020-03-01', '2021-06-01']

# 문자열 데이터(시리즈 객체)를 판다스 Timestamp로 변환
ts_dates = pd.to_datetime(dates)   
print(ts_dates)
print('\n')

# Timestamp를 Period로 변환
pr_day = ts_dates.to_period(freq='D')
print(pr_day)
pr_month = ts_dates.to_period(freq='M')
print(pr_month)
pr_year = ts_dates.to_period(freq='A')
print(pr_year)

#인덱스: DatetimeIndex가 PeriodIndex로 변환
#freq 옵션: D-하루, w-한달, A- 1년(1년이 끝나는 12월 기준)
#이 외에도 다양한 옵션 존재, p206