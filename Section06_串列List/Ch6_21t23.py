'''
刪除空白字元rstrip()/lstrip()/strip()

刪除字串開始或結尾多於空白是一個很好用的方法，特別是系統要求讀者輸入資料時，一定會有人不小心多輸入了一些空白字元，此時可以用這個方法刪除多餘的空白。
'''

# Ch6_21.py 刪除開始端與結尾端多於空白的應用

strN = " helloworld "
strL = strN.lstrip() #刪除字串左邊空白
strR = strN.rstrip() #刪除字串右邊空白
strB = strN.rstrip().lstrip() #刪除右邊空白再刪除左邊空白
strO = strN.strip() #刪除兩邊空白
print("/%s/" % strN)
print("/%s/" % strL) 
print("/%s/" % strR) 
print("/%s/" % strB) 
print("/%s/" % strO)

# Ch6_22.py 沒有使用strip()與有使用strip()方法處理讀取字串的觀察
# string = input("請輸入名字: ")
# print("/%s/" % string)
# string = input("請輸入名字: ")
# print("/%s/" % string.strip())

# Ch6_22_1.py 活用python程式
# string = input("請輸入名字: ")
# print("/%s/" % string)
# string = input("請輸入名字: ").strip()
# print("/%s/" % string)
# string = input("請輸入名字: ").strip().title()
# print("/%s/" % string)

'''
格式化字串位置 center()/ljust/rjust/zfill()
'''
# Ch6_23.py 格式化字串位置的應用
title = "Queensland University of Technology"
print("/%s/" % title.center(50))
dt = "Department of ME"
print("/%s/" % dt.ljust(50))
site = "Ey Fantastic"
print("/%s/" % site.rjust(50))
print("/%s/" % title.zfill(50)) #格子共50格, 其他的前面補0