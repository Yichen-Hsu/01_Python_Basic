'''
在串列末端增加元素 append()

方法一:
增加新的元素方式可以是 再寫一個新的列表元素，然後再相原本的串列做相加得到新串列，就可以得到增加串列元素的目的。

方法二:
使用append()方法 新增元素
'''

# method 1:
from re import A


k = ['yota']
l = ['fenda', 'penda', 'kenda']
print(k+l)

# method2:
k= ['yota']
k.append('fenda')
k.append('penda')
k.append('kenda')
print(k)

# Ch6_24.py 先建立一個空串列，然後分別使用append()增加3筆元素內容。
cars = []
print("目前串列內容 = ", cars)
cars.append('Honda')
print("目前串列內容 = ", cars)
cars.append('Toyota')
print("目前串列內容 = ", cars)
cars.append('Posh')
print("目前串列內容 = ", cars)

'''
有時候在程式設計時須預留串列空間，未來在使用附值方式將數值存入串列，可以使用下列方式處理。
'''

l = [None] * 3     # 此方法要知道你要給list有多少元素
l[0] = 'a'
l[1] = 2
l[2] = 'umbrealla'

print(l)

