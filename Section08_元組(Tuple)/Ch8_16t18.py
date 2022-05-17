'''
使用Zip()打包多個物件

這是一個內鍵函數，參數內容主要是2個或多個可迭代的物件，如果有存在多個物件(例如串列或元組)，可以用zip()將多個物件打包成ZIP物件，然後未來視需要將此zip物件轉成串列或其他物件。
'''

# Ch8_16.py zip的應用
fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)
print(zipData)
print(type(zipData))
player = list(zipData)
print(player)
new_list = enumerate(player)
print(list(new_list))


'''
如果放在zip()函數的串列參數，長度不相等，由於多出的元素無法匹配，轉成串列物件後zip物件元素數量是較短的數量
'''

# Ch8_17.py fields串列元素數量是3個， info串列數量元素數只有2個， 最後 zip 物件元素數量是2個。

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30']
zipData = zip(fields, info)
print(zipData)
print(type(zipData))
player = list(zipData)
print(player)


'''
如果在zip()函數內增加'*'符號，相當於可以unzip()串列。
'''

# Ch8_18.py 恢復zip前的串列

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)
print(zipData)
print(type(zipData))
player = list(zipData)
print(player)

f, i = zip(*player)
print('fields =', f)
print('info = ', i)