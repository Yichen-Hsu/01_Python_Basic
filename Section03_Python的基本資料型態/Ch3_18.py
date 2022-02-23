'''
str()函數有好幾個用法:
可以設定空字串。
'''
x = str() #設定空字串
print(x)

'''
設定字串
'''
x = str('abc')
print(x)

'''
可以強制將數值資料轉換為字串資料
'''
x = 123
y = str(x)
print(y)

#Ch3_18.py: 使用str()函數將數值資料強制轉換為字串的應用
num1 = 222
num2 = 333
num3 = num1 + num2
print('這是數值相加')
print(num3)
str1 = str(num1) + str(num2)
print('強制轉換數值為字串相加')
print(str1)

'''
555是數值資料 222333則是一個字串
'''
print(type(num3))
print(type(str1))
