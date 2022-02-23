'''
如果要精確地使用python內建的math模組，使用前需要導入模組，未來可以更精確的使用
請使用math模組的pi，重新設計CH2_7
'''

import math

r = 5
print('圓面積:單位是平方公分')
area = math.pi * r * r
print(area)

circumference = 2 * math.pi * r
print("圓周長:單位是公分")
print(circumference)


