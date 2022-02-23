'''
{} 和 format() 函數
'''

# Ch4_11.py
score = 90
name = "Ey"
count = 1
print("{}你的第{}次物理考試成績是{}".format(name, count, score))

# Ch4_12.py
score = 90
name = "Ey"
count = 1
string = "{}你的第{}次物理考試成績是{}"
print(string.format(name, count, score))

# Ch4_13.py 在{}內增加編號
score = 90
name = "Ey"
count = 1
print("{0}你的第{1}次物理考試成績是{2}".format(name, count, score))

# Ch4_13.py 在{}使用具名的參數
print("{n}你的第{c}次物理考試成績是{s}".format(n="Ey", c=1, s=90)) # note: 使用具名參數時，具名參數部分必須放在format()參數的左邊，若以此例為例，若將n和c位置對調將會產生錯誤。

# Ch4_15.py 計算圓面積，同時格式化輸出。
r = 5
PI = 3.14159
area = r**2*PI
print("/半徑{0:3d}圓面積是{1:10.2f}/".format(r, area))

# Ch4_16.py 輸出對齊方式的應用
print("/半徑{0:>3d}圓面積是{1:>10.2f}/".format(r, area))
print("/半徑{0:<3d}圓面積是{1:<10.2f}/".format(r, area))
print("/半徑{0:^3d}圓面積是{1:^10.2f}/".format(r, area))

# Ch4_17.py 填充字元的應用
title = "南極旅遊講座"
print("/{0:*^20s}/".format(title))

'''
上述使用format()和{}搭配的優點是，使用Python應用在網路爬蟲時，我們的設計可以簡化、易懂和不容易出錯
'''

# Ch4_18.py 以傳統和format()方式實作網路爬蟲會碰上的類似網址
url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type = "school"
print(url + city + "&radius=" + str(r) + "&type=" + type)
print(url + "{}&radius={}&type={}".format(city, r, type))