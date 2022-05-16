'''
其他常用的元組方法

max(tuple) 獲得內容最大值
min(tuple) 獲得內容最小值
'''
# Ch8_12.py 元組內建方法max()、min()的應用
tup = (1, 3, 5, 7, 9)
print(f'tup的最大值是 {max(tup)}')
print(f'tup的最小值是 {min(tup)}')


'''
enumerate 物件使用在元組

當enumerate()方法產生的物件轉成串列時，其實此串列的配對元素是元組
'''

# Ch8_13.py 測試enumerate物件轉成串列後，原先的元素變成元組資料型態。
drinks = ['coffee', 'tea', 'wine']
enumerate_drinks = enumerate(drinks)
lst = list(enumerate_drinks)
print('轉成串列輸出, 初始索引直是0 = ', lst)
print(type(lst[0]))

# Ch8_14.py 將元組轉成enumerate物件，再轉回元組物件。
drinks = ('coffee', 'tea', 'wine')
enumerate_drinks = enumerate(drinks)
print('轉成元組輸出，初始值是 0 =', tuple(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)
print('轉成元組輸出，初始值是 10 =', tuple(enumerate_drinks))

# Ch8_15.py 將元組轉成enumerate物件，再解析這個enumerate物件
drinks = ('coffee', 'tea', 'wine')
# 解析enumerate物件
for drink in enumerate(drinks):
    print(drinks)
for count, drink in enumerate(drinks):
    print(count, drink)
print('*'*20)
# 解析enumerate物件
for drink in enumerate(drinks, start=10):
    print(drink)
for count, drink in enumerate(drinks, start=10):
    print(count, drink)