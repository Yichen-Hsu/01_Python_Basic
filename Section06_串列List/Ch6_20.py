'''
Python簡單的物件導向觀念

在物件導向的程式設計(Object Oriented Programming)觀念裡，所有資料皆算是一個物件(Object)。
例如，整數、浮點數、字串或是所提到的串列皆是一個物件。
我們可以為所建立的物件設計一些方法(method)，提供這些物件使用，在這裡所提的方法表面是函數，但是這函數釋放在類別內，我們稱之為方法，
他與函數呼叫方式不同。目前Python有一些基本物件，提供預設的方法，要使用這些方法可以在物件後先放小數點，再放方法名稱。

基本語法格式如下:
物件.方法()

下列是字串常用的方法:
lower():將字串轉成小寫字。
upper():將字串轉成大寫字。
title():將字串轉成地一個字母是大寫字，其他都是小寫字
swapcase(): 將字串所有大寫改小寫，小寫改大寫。
rstrip(): 刪除字串尾端多餘的空白
lstrip(): 刪除字串開始端多餘的空白
strip():刪除字串頭兩邊多餘的空白
center(): 字串在指定寬度置中對齊
rjust(): 字串在指定寬度靠右對齊
ljust(): 字串在指定寬度靠左對齊
zfill(): 可以設定字串長度，原字串靠右對齊，左邊多餘空間補0
'''

# Ch6_20.py 將upper()和title()應用在字串。
cars = ['bmw', 'benz', 'audi']
carF = "我開的第一部車是" + cars[1].title()
carN = "我現在開的車子是" + cars[0].upper()
print(carF)
print(carN)

# 使用lower字串實例
string = 'ABC'
print(string.lower())

# 使用title()時須留意，如果字串內含多個單字，所有單字的均是第一個字母大寫。
string = "i love python"
print(string.title())

# 下列是swapcase()的案例
string = 'Hello World'
print(string.swapcase())