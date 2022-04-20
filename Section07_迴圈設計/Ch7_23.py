'''
強制離開for迴圈 break指令
'''

# Ch7_23.py 輸入一系列數字，當輸入數字是5時，終止迴圈執行
print('test1')
for digit in range(0, 11):
    if digit == 5:
        break
    print(digit, end=', ')
print()
print('test2')
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end=', ')
