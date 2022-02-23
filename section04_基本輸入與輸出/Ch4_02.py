# Ch4_2.py: 重新設計Ch4_1.py，將兩筆資料在同一行輸出，彼此之間使用tab鍵的距離隔開。
num1 = 222
num2 = 333
num3 = num1 + num2
print("這是數值相加", num3, end="\t") #以tab鍵值位置分隔兩筆資料輸出
str1 = str(num1) + str(num2)
print("強制轉換為字串相加", str1, sep=" ooo ")
