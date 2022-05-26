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
