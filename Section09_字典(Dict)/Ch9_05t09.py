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