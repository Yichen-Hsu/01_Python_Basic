'''
---數值運算常用的函數---
下列數值是運算時常用的函數

abs() = 計算絕對值
pow(x,y) = 返回x的y次方
round(): 這是採用演算法則的Bankers rounding觀念，如果處理位數左邊是奇數則使用四捨五入，如果處理位數左邊是偶數則使用五捨六入
例如: round(1.5) = 2, 
      round(2.5) = 2

處理小數時，第2個參數代表取到小數第幾位，小數位數的下一個小數位採用5以下捨去，"51"以上進位。
例如: round(2.15,1) = 2.1
      round(2.25,1) = 2.2
      round(2.251,1) = 2.3
      round(2.151,1) = 2.2
'''
#Ch3_10.py
x = -10
print("以下輸出abs()函數的應用")
print(x)
print(abs(x))
x = 5
y = 3
print("以下輸出pow()函數的應用")
print(pow(x,y))
x = 47.5
print("以下輸出round(x)函數的應用")
print(x)
print(round(x))
x = 48.5
print(x)
print(round(x))
x = 49.5
print(x)
print(round(x))
print("以下輸出round(x,n)函數的應用")
x = 2.15
print(x)
print(round(x,1))
x = 2.25
print(x)
print(round(x,1))
x = 2.151
print(x)
print(round(x,1))
x = 2.251
print(x)
print(round(x,1))
'''
需要留意的是，使用上述abs()、powe()或round()函數，儘管可以得到運算的結果。
但是原先變數的值則是沒有改變的。
'''