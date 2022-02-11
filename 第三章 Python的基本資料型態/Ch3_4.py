'''
若某一個變數是整數，但最後所儲存的值是浮點數，Python也會將此變數轉成浮點數。
'''
#Ch3_4.py: 整數換成浮點數的應用
x = 10
print(x)
print(type(x))
x = x + 5.5
print(x)
print(type(x))