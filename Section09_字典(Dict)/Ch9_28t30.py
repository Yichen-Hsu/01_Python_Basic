'''
字典常用的函數和方法
'''

# Ch9_28.py 列出字典以及字典內的字典元素個數。

wechat_account = {
    'helloworld':{
        'last name':'Hsu',
        'first name':'Ey',
        'city':'Maioli'
    },
    'kevin':{
        'last name':'ken',
        'first name':'ni',
        'city':'one'
    }
}

print('wechat_account 字典元素個數: ', len(wechat_account))
print('wechat_account[helloworld] 字典元素個數: ', len(wechat_account['helloworld']))
print('wechat_account[kevin] 字典元素個數: ', len(wechat_account['kevin']))

'''
fromkeys()

這是建立一個字典的方法，它的語法格式如下:

mydict = dict.fromkeys(seql[, value])

上述會使用seq序列建立字典，序列內容將是字典的鍵，如果沒有設定value則用none當字典的值
'''

# Ch9_29.py 分別使用串列和元組建立字典。
# 將串列轉成字典
seq1 = ['name', 'city']
list_dict1 = dict.fromkeys(seq1)
print(f'字典1{list_dict1}')
list_dict2 = dict.fromkeys(seq1, 'Chicago')
print(f'字典2{list_dict2}')
# 將元組轉成字典
seq2 = ('name', 'city')
list_dict1 = dict.fromkeys(seq2)
print(f'字典1{list_dict1}')
list_dict2 = dict.fromkeys(seq2, 'New York')
print(f'字典2{list_dict2}')

'''
get()

搜尋字典的鍵，如果鍵存在則傳回該鍵的值，如果不存在則傳回預設值。

ret_value = mydict.gt(key[, default=none])

key 是要搜尋的鍵，如果找不到key則傳回default的值(如果沒設default值就傳回none)

'''

# Ch9_30.py get()方法的應用
fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print('Value = ', ret_value1)
ret_value2 = fruits.get('grape')
print('Value = ', ret_value2)
ret_value3 = fruits.get('grape', 10)
print('Value = ', ret_value3)



'''
setdefault()

這個方法基本上與get相同，不同之處在於get()方法不會改變字典內容。使用setdefault()方法時若所搜尋的鍵不在
會將"鍵:值"加入字典，如果有設定預設值則將鍵:預設值加入字典，如果沒有設定預設值則將鍵:None加入字典

ret_value = mydict.setdefault(key[, default=none]) #mydict 是欲搜尋的字典

'''

# Ch9_30_1.py setdefault()方法，鍵在字典內的應用
# key在字典內
fruits = {'Apple':20, "Orange":25}
ret_value = fruits.setdefault('Orange')
print('value = ', ret_value)
print('fruits字典', fruits)
ret_value = fruits.setdefault('Orange')
print('value = ', ret_value)
print('fruits字典', fruits)

# Ch9_30_2.py setdefault()方法，鍵不在字典內的應用。
person = {'name':'John'}
print('原先字典內容', person)

# age鍵不存在
age =person.setdefault('age')
print('增加age鍵', person)
print('age = ', age)

# sex鍵不存在
sex = person.setdefault('gender', 'Male')
print('增加gender鍵', person)
print('gender = ', sex)


