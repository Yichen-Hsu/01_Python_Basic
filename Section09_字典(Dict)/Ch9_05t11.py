'''
增加字典元素

可使用下列語法格式增加字典元素:

mydict[鍵] = 值 #mydict 是字典變數
'''

# Ch9_5.py 為fruits字典增加橘子一斤18元
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
fruits['橘子'] = 18
print(fruits)
print('橘子一斤 = ', fruits['橘子'], '元')

'''
在設計打鬥遊戲時，我們可以使用螢幕座標標記小兵的位置，下列實例適用xpos/ypos標記小兵的x座標/y座標
'''

# Ch9_6.py 為solider0字典增加x, y軸座標(xpos, ypos)和移動速度(speed)元素，同時列出結果驗證。
soldier0 = {'tag':'red', 'score':3}
soldier0['xpos'] = 100
soldier0['ypos'] = 30
soldier0['speed'] = 'slow'
print('小兵的x座標 = ', soldier0['xpos'])
print('小兵的y座標 = ', soldier0['ypos'])
print('小兵的移動速度 ', soldier0['speed'])

'''
更改字典元素內容

市面上的水果價格是浮動的，如果發生價格異動可以使用本節觀念更改。
'''

# Ch9_07.py 將fruits字典的香蕉一斤改成12元
fruits = {'香蕉':15, '西瓜':20, '水蜜桃':34}
print('舊價格香蕉一斤 =', fruits['香蕉'], '元')
fruits['香蕉'] = 12
print('新價格香蕉一斤 =', fruits['香蕉'], '元')

'''
在設計打鬥遊戲時，我們需要時時移動小兵的位置，此時可以使用本節觀念時時更改小兵的位置
'''
# Ch9_08.py 依照solider字典speed的鍵值更動小兵的位置。
soldier0 = {'tag':'red', 'score':3, 'xpos':100, 'ypos':30, 'speed':'slow'}
print('小兵的x, y舊座標 = ', soldier0['xpos'], ',', soldier0['ypos'])
if soldier0['speed'] == 'slow':
    x_move = 1
elif soldier0['speed'] == 'medium':
    x_move = 3
else:
    x_move = 5
soldier0['xpos'] += x_move
print('小兵的x, y新座標 = ', soldier0['xpos'], ',', soldier0['ypos'])

'''
上述程式將小兵的移動速度分成3個等級, slow是每次xpos移動1單位, medium是3單位, 另一等級則是5單位
'''

'''
刪除字典特定元素

如果想要刪除字典的特定元素，他的語法格式如下:
del_mydict['鍵'] 
'''
# Ch9_09.py 刪除fruits字典的西瓜元素:
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print('舊fruits字典內容', fruits)
del fruits['西瓜']
print(f'新fruits的字典是{fruits}')

'''
字典pop()的方法

python字典的pop()方法可以刪除字典內特定的元素, 同時傳回所刪除的元素，它的語法格式如下:

ret_value = dictObj.pop(key[, default])

上述key是要搜尋刪除的元素的鍵，找到時就將該元素從字典內刪除，同時將刪除鍵的值回傳。
當找不到key時則回傳default設定的內容，如果沒有設定則導致keyError，程式異常終止。
'''

# Ch9_09_1.py 刪除字典元素同使可以傳回所刪除字典元素的應用
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print('舊fruits字典內容', fruits)
objKey = '西瓜'
value = fruits.pop(objKey)
print('新frutis字典內容', fruits)
print('刪除內容: ', objKey + ':' + str(value))

# ex01 所刪除的元素不存在，導致'keyerror'，程式異常終止。
'''
num = {'a':1, 'b':2}
value = num.pop('c')
'''

# ex02 所刪除的元素不存在, 列印 'does not exit'字串
num = {'a':1, 'b':2}
value = num.pop('c', 'does not exit')
print(value)

'''
字典的popitem()方法

python字典的popitem()方法可以隨機刪除字典內的元素，同時傳回所刪除的元素，所傳回的是元組(key, value), 它的語法格式如下:
valueTap = dictObj.popitem() #可隨機刪除字典的元素
如果字典是空的，會有錯誤異常產生
'''

# Ch9_09_2.py 列出所隨機刪除的字典元素內容。
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print('舊fruits的字典內容', fruits)
valueTup = fruits.popitem()
print('新fruits字典內容', fruits)
print('刪除的內容', valueTup)


'''
刪除字典所有的元素

python有提供方法clear()可以將字典的所有元素刪除，此時字典仍然存在，不過將變成空的字典。
'''
# Ch9_10.py 使用clear()方法刪除fruits字典的所有元素。
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print('舊的字典元素內容', fruits)
fruits.clear()
print('新的字典元素內容', fruits)


'''
刪除字典

python 也有提供del指令可以將整個字典刪除，字典一，字典一經刪除就不存在。他的語法格式如下:
del mydict #可刪除的字典
'''
# Ch9_11.py 刪除字典的測試，這個程式前4行是沒有任何問題，第5行嘗試列印已經被刪除的字典，所以產生錯誤，錯誤原因是沒有定義的字典。
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print('舊的字典元素內容', fruits)
del fruits
print('新的字典元素內容', fruits)
