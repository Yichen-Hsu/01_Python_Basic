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
