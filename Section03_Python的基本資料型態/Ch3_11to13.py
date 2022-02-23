#科學記號表示法
'''
科學記號表示法如下: a * 10^n
例: 123456
    科學記號為 1.23456 * 10^5
    python記號為 1.23456e+5 or 1.23456E+5
    
    0.123456
    科學記號為  1.23456 * 10^-1
    python記號為 1.23456e-1 or 1.23456E-1

而複數(complex number)
python支持複數的使用，複數是由實數部分(real)及虛數部分(imag)所組成。
例如: a + bj or complex(a,b) 其中 實部的a 及 虛部的b 皆為浮點數
'''


"""
布林值資料型態

基本觀念
Python的布林值(Boolean)資料型態有兩種，True(真)或False(偽)
資料型態代號為 bool

布林值一般是應用在程式流程的控制，特別是在條件運算式中，程式可以根據這個布林值判斷應該如何執行工作
"""

#Ch3_11.py 列出布林值True與布林值False的資料型態
x = True
print(x)
print(type(x)) #列出x資料型態

y = False
print(y)
print(type(y)) #列出y資料型態

'''
如果將布林值資料型態強制轉換成整數，如果原值是True，將得到 1。 如果原值是False，將得到 0 。
'''
#Ch3_12.py 將布林值強制轉換為整數，同時列出轉換的結果
x = True
print(int(x))
print(type(x))
y = False
print(int(y))
print(type(y))

'''
有時候也可以將布林值當作數值資料，因為 True & False 會被視為 1 與 0
'''

#Ch3_13.py 將布林值與整數值相加的應用，並觀察最後變數資料型態，讀者可以發現，最後的變數資料型態是整數值
xt = True
x = 1 + xt
print(x)
print(type(x))

yt = False
y = 1 + yt
print(y)
print(type(y))

'''
3-3-2 bool()

這個bool()函數可以將所有資料轉成 True 或 False
我們可以將資料放在此函數得到布林值，數值如果是 0 或是 空 的資料則會被視為 False

'''

a = bool(0)
print(a)
b = bool(0.0)
print(b)
c = bool(())
print(c)
d = bool([])
print(d)
e = bool({})
print(e)

'''
至於其他皆會被視為True
'''
f = bool(1)
print(f)
g = bool(-2)
print(g)
h = bool({1,2,3,4})
print(h)