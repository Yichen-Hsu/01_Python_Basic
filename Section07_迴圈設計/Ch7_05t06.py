'''
如果for迴圈的程式碼區塊有多行敘述時，要留意這些敘述同時需要做縮排處理。語法格式如下：

for var in 可迭代物件：
    程式碼
    ....
'''

# Ch7_05.py 這個程式在設計時，首先筆者將串列的元素英文名字全部改成小寫，然後for迴圈的程式碼區塊是有2行，這2行(第4和5行)皆需內處理，player.title()的title()方法可以處理第一個字母以大寫顯示。
players = ['curry', 'jordan', 'james', 'durant', 'obama']
for player in players:
    print(f'{player.title()}, it was a great game.')
    print(f'我迫不急待想看下一場比 {player.title()}')

# Ch7_06.py Python也允許將for迴圈應用在擷取的區間串列元素上。
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
print("列印前3位球員")
for player in players[:3]:
    print(player)
print("列印後3位球員")
for player in players[-3:]:
    print(player)
