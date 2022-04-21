'''
強制離開for迴圈 break指令
'''

# Ch7_23.py 輸入一系列數字，當輸入數字是5時，終止迴圈執行
print('test1')
for digit in range(0, 11):
    if digit == 5:
        break
    print(digit, end=', ')
print()
print('test2')
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end=', ')
print()

# Ch7_24.py 列出球員名稱，列出多少個球員則是由螢幕輸入，這個程式同時設定，如果螢幕輸入的人數大於串列的球員時，自動將所輸入的人數降為串列的球員數。
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = int(input("請輸入人數: "))
if n > len(players) : n = len(players)
index = 0
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index += 1
print()

# Ch7_25.py 一個串列scores內含有10個分數元素，請列出最高分的前5個成績。
scores = [94, 82, 60, 91, 88, 79, 61, 93, 99, 77]
scores.sort(reverse = True)
count = 0
for sc in scores:
    count += 1
    print(sc, end= " ")
    if count == 5:
        break
