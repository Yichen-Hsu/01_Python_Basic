'''
取得字典元素數量

在串列(list)或元組(tuple)使用的方法len()也可以應用在字典，他的語法如下:
length = len(mydict) #將傳回mydict字典的元素數量給length
'''
# Ch9_14.py 列出空字典和一般字典的元素數量，本程式第4行由於是建立空字典，所以第7行印出元素是0
fruits = {'西瓜': 15, '香蕉':20, '水蜜桃':25, '蘋果':18}
noodles = {'牛肉麵':100, '肉絲麵': 80, '陽春麵':60}
empty_dict = {}
print('fruits字典元素數量 = ', len(fruits))
print('noodels字典元素數量 = ', len(noodles))
print('empty_dict字典元素數量 = ', len(empty_dict))


'''
驗證元素是否存在

鍵 in mydict #可驗證鍵元素是否存在
'''
# Ch9_15.py 這個程式會要求輸入'鍵:值', 然後判斷此元素是否在fruits字典，如果不在字典則將此"鍵:值"加入字典。
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':26}
key = input('請輸入鍵值(key)')
value = int(input('請輸入值(value) = '))
if key in fruits:
    print(f'{key}已經在字典裡了')
else:
    fruits[key] = value
    print('新的fruits字典內容 = ', fruits)