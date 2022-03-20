'''
for 迴圈可以讓程式將整個物件遍歷，又稱迭代。在遍歷期間，同時可以記錄或輸出每次遍歷的狀態或稱軌跡。

可迭代物件(iterable object)可以是串列、元組、字典與集合或range()。
資訊中迭代(iteration)可以解釋為重複執行敘述，直到每個元素皆被執行一次，整個迴圈才會停止。
'''

# Ch7_03.py NBA球隊有5位球員，分別是Hamburger, Loki, Raspberry Pi, James, Banana。 要列出這些球員就很適合使用for迴圈執行這個工作。
players = ['Hamburger', 'Loki', 'Raspberry Pi', 'James', 'Banana']
for player in players:
    print(player)