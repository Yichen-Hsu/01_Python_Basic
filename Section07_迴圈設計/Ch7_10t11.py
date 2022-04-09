'''
活用for迴圈
'''

# ex.
string = 'abc'
for i in dir(string):
    print(i)

'''
range()函數

Python 可以使用range()函數產生一個等差級序列，我們又稱這等差級序列為可以迭代物件。
也可以稱是range物件。由於range()是產生等差級序列。我們可以直接使用，將此等差級序列當作環圈的計數器。

range()的用法與串列的切片類似

range(start, stop, step)

stop是唯一必須的值，請參考以下範例。
'''
# ex.
for i in range(5):
    print(i)
print('-'*30)
for i in range(1, 5):
    print(i)
print('-'*30)
for i in range(1, 10, 2):
    print(i)
print('-'*30)
for i in range(9, -3, -2):
    print(i)
print('-'*30)

# Ch7_10.py 輸入數字，本程式會將此數字當作列印星星的數量。
for i in range(int(input())):
    print('*', end='')

# Ch7_11.py 銀行存款複利的累積軌跡
money = 50000
rate = 0.015
n = 5
for i in range(5):
    money *= (1+rate)
    print(f'第{i+1}年本金和: {int(money)}')