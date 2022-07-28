# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

student1 = pd.Series({'국어': np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})
print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 과목별 점수로 사칙연산 수행(연산 메소드 사용)
# 연산 메소드에 fill_value=0 옵션을 설정해 std1의 국어 점수와 std2의 영어 점수는 NaN 대신 0으로 입력된다.
sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)
print(type(sr_div))
print('\n')

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result)