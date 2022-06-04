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