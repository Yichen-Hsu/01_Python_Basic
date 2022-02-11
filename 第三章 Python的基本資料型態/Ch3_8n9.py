'''
設計程式時，可以自行強制使用下列函數，轉換變數的資料型態。
int() = 將資料型態強制轉為整數
float() = 將資料型態強制轉為浮點數
'''

#Ch3_8.py
x = 10.5
print(x)
print(type(x)) #加法前列出X資料型態
y = int(x) +5 
print(y)
print(type(y)) #加法後列出y資料型態


#Ch3_9.py
a = 10
print(a) 
print(type(a)) #加法前列出X資料型態
b = float(a) +12
print(b)
print((type(b))) #加法後列出Y資料型態