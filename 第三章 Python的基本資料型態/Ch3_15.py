'''
3-4-1 字串的連接

數學的運算子"+", 可執行兩個字串相加，產生新的字串
'''

#Ch3_15.py 字串連接的應用

num1 = 222
num2 = 333
num3 = num2 + num1
print("以下是數值相加")
print(num3)
numstr1 = "222"
numstr2 = "333"
numstr3 = numstr1 + numstr2
print("以下是由數值組成的字串相加")
print(numstr3)
numstr4 = numstr1 + " " + numstr2
print("以下是由數值組成的字串相加，同時中間加上一空格")
print(numstr4)
str1 = "Deepmind "
str2 = "Deepen your mind"
str3 = str1 + str2
print("以下是一般字串相加")
print(str3)
