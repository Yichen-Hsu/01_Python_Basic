'''
基礎的統計應用

假設有一組數據，此數據有n筆資料，我們可計算它的平均值、變異數、標準差
'''
# Ch8_20.py 計算5, 6, 8, 9的平均值、變異數和標準差
# 計算平均值
vals = (5, 6, 8, 9)
mean = sum(vals) / len(vals)
print('平均值: ', mean)

# 計算變異數
var = 0
for v in vals:
    var += ((v - mean)**2)
var = var / (len(vals))
print('變異數: ', var)

# 計算標準差
dev = 0
for v in vals:
    dev += ((v - mean)**2)
dev = (dev / (len(vals)))**0.5
print('標準差: ', dev)

'''
多重指定、打包與解包

在程式的開發術語中我們可以將串列、元組、字典、集合等稱容器，在多重指定中，等號左右兩邊也可以是容器，只要他們的結構相同即可。
例如:
    x, y = (29, 10)
專業程式設計的術語稱元組解包(tuple unpacking)，然後將元素內容設定給對應的變數。

a, b, *c = 1, 2, 3, 4, 5
上述我們稱多的3, 4, 5將打包(packing)成串列c

在多重指定中等號兩邊可以是容器，例如:
    [a, b, c] = (1, 2, 3)
上述並不是更改將 1, 2, 3設定給串列造成更改串列內容，而是將兩邊都解包，所以可以得到a, b, c分別是1, 2, 3
Python處理解包時，也可以將此解包應用在多維度的容器，只要兩邊容器的結構相同即可。
'''

[a, [b, c]] = (1, (2, 3))
print(a, b, c)

'''
容器的解包主要是可以在程式設計時避免多重索引造成程式閱讀困難，我們可以用更容易了解方式閱讀程式。
'''

# Ch8_21.py for迴圈解包物件的應用
fields = ['台北', '台中', '高雄']
info = [80000, 56999, 39999]
zipData = zip(fields, info)
sold_info = list(zipData)
for city, sales in sold_info:
    print(f'{city} 銷售金額是 {sales}')


'''
再談 bytes 與 bytearray

bytes: 內容是不可變，可以想成是串列，可以使用bytes()將串列內容轉成bytes資料

bytearray: 內容是可變，可以想成是元組，可以使用bytearray()將串列內容轉乘bytearray資料。
'''

x = [1, 2, 3, 4, 255]
x_bytes = bytes(x)
print(x_bytes)

x = [1, 2, 3, 4, 255]
x_bytearray = bytearray(x)
print(x_bytearray)