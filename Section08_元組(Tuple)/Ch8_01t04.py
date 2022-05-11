'''
在大型商業或遊戲網站設計中，串列(list)是非常重要的資料型態，因為記錄各種等級客戶、遊戲腳色...等，皆須使用串列，串列資料可以隨時變動更新。
Python提供另一種資料型態稱元祖(Tuple)，這種資料型態結構與串列完全相同。
元祖與串列最大的差異是，他的元素值與元素個數不可更動，有時又可稱不可改變的串列。
'''

'''
元祖的定義

元祖的定義是將元素放在小括號內 "()"
下列是元祖的語法格式。

mytuple = (元素1, 元素2, 元素3...)

基本上元祖的每一筆資料稱元素，元素可以是整數、字串、或串列...等，這些元素放在小括號內()，彼此用逗號隔開
如果要列印元祖的內容，可以使用print()函數，將元祖名稱當作變數名稱即可。

如果元祖內的元素只有一個，在定義時需在元素右邊加上逗號
'''

# Ch8_01.py 定義與列印元祖，最後使用type()列出元祖資料型態。
numbers1 = (1, 2, 3, 4, 5)
fruits = ('Apple', 'Lemon')
mixed = ('Ey', 50, 50)
val_tuple = ('single',)
print(numbers1)
print(fruits)
print(mixed)
print(val_tuple)
# 列出元祖資料型態
print('元祖mixed資料型態是: ', type(mixed))

'''
另外一個簡便建立元祖有多個元素的方法是，用等號，右邊有一系列元素，元素彼此用逗號隔開。
'''

x = 5, 6, 5, 6, 8, 9
print(type(x))
print(x)


'''
讀取元組元素"()"，如果想要讀取元組內容和串列是一樣的用中括號"[]"。在Python中元組元素是從索引直0開始配置。所以如果是元組的第一筆元素，索引直是0
第二筆元素索引直是1，依此類推，如下所示:

mytuple[i]  #讀取索引i的元祖元素
'''

# Ch8_02.py 讀取元組元素，與一次指定多個變數值得應用
numbers1 = (1, 2, 3, 4, 5)
fruits =('apple', 'orange')
val_tuple = (10,)
print(numbers1[0])
print(numbers1[4])
print(fruits[0], fruits[1])
print(val_tuple[0])
x, y = ('apple', 'orange')
print(x, y)
x, y = fruits
print(x, y)

'''
遍歷所有元組元素
'''
# Ch8_3.py  假設元組是由字串和數值組成，這個程式會列出元組所有元素內容。
keys = ('magic', 'xaab', 9099) #定義元組元素是字串與數字
for key in keys:
    print(key)

'''
修改元組內容產生錯誤的實例

元組元素內容不可被修改，因此會產生程式錯誤
'''
# Ch8_4.py 修改元組內容產生錯誤的實例
fruits = ('apple', 'orange') #定義元組元素是字串
print(fruits[0]) #列印元組fruits[0]
fruits[0] = 'watermelon' #將元素內容改為watermelon
print(fruits[0]) #列印元組fruits[0]