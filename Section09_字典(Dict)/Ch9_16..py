'''
設計字典的可讀性技巧

設計大型程式的實務上，字典的元素內容很可能是由長字串所組成，碰上這類情形，建議從新的一行開始安置每一個元素
如此可以大大增加字典的可讀性。
'''

# Ch9_16.py 字典元素的長字串的應用
players = {
    'Stephen Curry': 'Golden State Warrior',
    'Kevin Durant': 'Golden State Warrior',
    'Labron James': 'Cleveland Cavaliers',
    'James Harden': 'Houston Rockets',
    'Paul Gasol': 'San Antonio Spurs'
}

print('Stephen Curry 是', players['Stephen Curry'] ,'的球員')
print('Kevin Durant 是', players['Kevin Durant'] ,'的球員')
print('Paul Gasol 是', players['Paul Gasol'] ,'的球員')


'''
合併字典update()與使用**新方法

如果想要將2個字典合併可以使用update()方法。
'''

# Ch9_16_1.py 字典合併的應用，經銷商A(dealerA)銷售Nissan、Toyota和Lexus等三個品牌的車子，經銷商B銷售BMW和Benz等兩個品牌的車子，設計程式當經銷商A併購了經銷商B後，列出經銷商A所銷售的車子
dealerA = {1: 'Nissan', 2: 'Toyota', 3: 'Lexus'}
dealerB = {11: 'BMW', 12:'Benz'}
dealerA.update(dealerB)
print(dealerA)

'''
在合併字典時，特別須注意的是，如果發生鍵(key)相同則第2個字典的值可以取代原先字典的值，所以設計字典合併時要特別注意。
'''

# Ch9_16_2.py 重新設計Ch9_16_1.py, 經銷商A和經銷商B所銷售的汽車品牌發生鍵相同，造成經銷商A併購經銷商B時，原先經銷商A銷售的汽車品牌被覆蓋，這個程式原先經銷商A銷售的Lexus品牌將被覆蓋。
dealerA = {1: 'Nissan', 2: 'Toyota', 3: 'Lexus'}
dealerB = {3: 'BMW', 4:'Benz'}
dealerA.update(dealerB)
print(dealerA)

'''
在python3.5以後的版本，合併字典新方法是使用{**a, **b}
'''

# ex01 合併字典的新方法
a = {1: 'Nissan', 2: 'Toyota'}
b = {3: 'Lexus', 4: 'BMW'}
print({**a, **b})

# ex02 也可以用在兩個以上的合併
a = {1: 'Nissan', 2: 'Toyota'}
b = {3: 'Lexus', 4: 'BMW'}
c = {5: 'Benz'}
print({**a, **b, **c})

'''
在資料處理中我們可能會碰上雙值序列的資料，如下所示:

[['日本','東京']], ['泰國','曼谷'], ['英國','倫敦']]

上述是普通的鍵/值序列，我們可以使用dict()將此序列轉成字典，其中雙值序列的第一個鍵，第二個是值。
'''

#Ch9_16_3.py 將雙值序列的串列轉成字典
nation = [['日本','東京'], ['泰國','曼谷'], ['英國','倫敦']]
nationDict = dict(nation)
print(nationDict)

'''
如果上述元素是原組(tuple)，例如:('日本','東京')也可以完成相同的工作。
'''

#ex01 將雙值序列的串列轉成字典，其中元素是元組(tuple)。
x = [('a','b'), ('c','d')]
y = dict(x)
print(y)

#ex02 下列是雙值序列是元組(tuple)的其他實例。
x = ('ab','cd','ed')
y = dict(x)
{'a':'b', 'c':'d', 'e':'d'}

'''
再談zip()
其實我們也可以使用zip()快速建立字典。
'''

#ex01 zip的應用1
mydict = dict(zip('abcde', range(5)))
print(mydict)

#ex02 zip的應用2
mydict = dict(zip(['a','b','c'], range(3)))
print(mydict)