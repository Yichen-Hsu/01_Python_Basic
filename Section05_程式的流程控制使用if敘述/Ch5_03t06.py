# Ch5_3.py 重新設計 Ch5_1.py，多了年齡滿20歲時的輸出
age = input("請輸入年齡: ")
if (int(age)) < 20:
    print("你的年齡太小了")
    print("須年滿20歲才可以購買菸酒")
else:
    print("歡迎購買菸酒")

# Ch5_4.py 奇數偶數的判斷
print("奇數偶數判斷")
num = eval(input("請輸入任意整數: "))
rem = num % 2
if (rem == 0):
    print(f"{num}是偶數")
else:
    print(f"{num}是奇數")

# PEP8 使用方法
if rem:
    print(f"{num}是奇數")
else:
    print(f"{num}是偶數")

# 高手寫法
print(f"{num}是奇數" if rem else f"{num}是偶數")

# Ch5_5.py
x, y = eval(input("請輸入兩個數字: "))
max_ = x if x > y else y
print(f"方法 1 最大值是: {max_}")
max_= max(x, y)
print(f"方法 2 最大值是: {max_}")
min_ = x if x < y else y
print(f"方法 1 最小值是: {min_}")
max_= min(x, y)
print(f"方法 2 最小值是: {min_}")

# Ch5_6.py
items = eval(input("請輸入1個數字: "))
items = 10 if items >= 10 else items
print(items)