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