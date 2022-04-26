'''
巢狀while迴圈
'''

# Ch7_35.py 使用while迴圈重新設計Ch7_21.py 列印9*9乘法表
i1 = 1
while i1 < 10:
    i2 = 1
    while i2 < 10:
        times = i1 * i2
        print(f'{i1}*{i2} = {times}', end=" ")
        i2 += 1
    print()
    i1 += 1