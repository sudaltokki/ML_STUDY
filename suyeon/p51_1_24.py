# -*- coding: utf-8 -*-
"""
p51,1-24
"""
import pandas as pd
import numpy as np

student1=pd.Series({'국어':np.nan, '영어':80,'수학':90})
"""직접 특정 위치에 nan을 입력하고 싶다면 numpy를 import한 후 사용"""
student2=pd.Series({'국어':90,'수학':80})

print(student1)
print('\n')
print(student2)
print('\n')

sr_add=student1.add(student2, fill_value=0)
sr_sub=student1.sub(student2, fill_value=0)
sr_mul=student1.mul(student2, fill_value=0)
sr_div=student1.div(student2, fill_value=0)

result=pd.DataFrame([sr_add,sr_sub,sr_mul,sr_div], index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)

"""0이 아닌 수/0  시 무한대라는 값이 오류가 나지 않고 표시됨. inf""" 