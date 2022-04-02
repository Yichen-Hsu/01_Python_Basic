'''
is 或 is not 運算式

可以用於比較兩個物件是否相同，所謂相同並不是只是內容相同，而是指物件變數指向相同的記憶體，物件可以是變數、字串、串列、元組、字典。
語法格式如下:

bool_value = obj1 is obj2      #物件obj1等於物件obj2內會傳回True
bool_value = obj1 is not obj2  #物件obj1不等於物件obj2內會傳回True
'''

'''
id() 可以獲得變數的位址，也可以獲得整數及浮點數變數在記憶體中的位址。
如果兩個整數(或浮點數)變數內容相同，他們會使用相同的記憶體位址儲存此變數。
'''

# Ch6_53.py
x = 10
y = 10
z = 15
r = 20

print(f'x = {x}, y = {y}, z = {z}, r = {r}')
print(f'x位址 = {id(x)}, y位址 = {id(y)}, z位址= {id(z)}, r位址 = {id(r)}')

r = x

print(f'x = {x}, y = {y}, z = {z}, r = {r}')
print(f'x位址 = {id(x)}, y位址 = {id(y)}, z位址= {id(z)}, r位址 = {id(r)}')

'''
因此可以知道 r = x 時 r 讀取整數的記憶體位址與x和y相同了
'''

# Ch6_54.py
x = 10
y = 10
z = 15
r = z -5
bool_value = x is y
print(f'x位址 = {id(x)}, y位址 = {id(y)}')
print(f'{x = }, {y = }, {bool_value}')

bool_value = x is z
print(f'x位址 = {id(x)}, z位址 = {id(z)}')
print(f'{x = }, {z = }, {bool_value}')

bool_value = x is r
print(f'x位址 = {id(x)}, r位址 = {id(r)}')
print(f'{x = }, {r = }, {bool_value}')

bool_value = x is not y
print(f'x位址 = {id(x)}, y位址 = {id(y)}')
print(f'{x = }, {y = }, {bool_value}')

bool_value = x is not z
print(f'x位址 = {id(x)}, z位址 = {id(z)}')
print(f'{x = }, {z = }, {bool_value}')

bool_value = x is not r
print(f'x位址 = {id(x)}, r位址 = {id(r)}')
print(f'{x = }, {r = }, {bool_value}')

# Ch6_55.py 拷貝後的新物件，位址及更改，即使內容相同，在使用is指令測試時，不同位址的串列會被視為不同的串列。
mysports = ['basketball', 'baseball']
sports1 = mysports
sports2 = mysports[:]
print(f'我喜歡的運動 = {mysports}', f'位址是 = {id(mysports)}')
print(f'運動 1 = {sports1}', f'位址是 = {id(sports1)}')
print(f'運動 2 = {sports2}', f'位址是 = {id(sports2)}')
bool_value = sports1 is mysports 
print('我喜歡的運動 is 運動1 = ', bool_value)
bool_value = sports2 is mysports 
print('我喜歡的運動 is 運動2 = ', bool_value)
bool_value = sports1 is not mysports 
print('我喜歡的運動 is not 運動1 = ', bool_value)
bool_value = sports2 is not mysports 
print('我喜歡的運動 is not 運動2 = ', bool_value)

'''
將 is 應用在None

None 是一個尚未定義的值，這是NoneType資料型態，在布林值中會被視為False，但是並不是空值。
'''
l = []
if l is None:
    print("l is none")
else:
    print('l is not none')