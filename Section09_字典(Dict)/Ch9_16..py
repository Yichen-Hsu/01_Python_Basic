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
