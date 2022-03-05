# Ch6_02.py 讀取串像元素的應用

james = [23, 19, 22, 31, 18]
print("列印james第1場得分: ", james[0])
print("列印james第2場得分: ", james[1])
print("列印james第3場得分: ", james[2])
print("列印james第4場得分: ", james[3])
print("列印james第5場得分: ", james[4])

'''

'''

# Ch6_03.py 一個傳統處理串列元素內容方式，與Python多重指定觀點的應用
james = [23, 19, 22, 31, 18]
game_1 = james[0]
game_2 = james[1]
game_3 = james[2]
game_4 = james[3]
game_5 = james[4]
print("列印james各場次得分: ", game_1, game_2, game_3, game_4, game_5)

# 高手設計方式
game1, game2, game3, game4, game5 = james
print("列印james各場次得分: ", game1, game2, game3, game4, game5)

'''
在程式設計時，常會需要取得串列前幾個元素、後幾個元素、某區間元素或是依照一定規則排序的元素，所取得的系列元素也可稱字串列，
這個觀念稱為 串列切片(List slices)。

ex:
    mylist[start:end] #讀取索引start到end-1索引的串列元素
    mylist[:end] #取得串列最前面到end-1名
    mylist[start:-n] #取得串列前面，不含由後數來最後n名。
    mylist[start:] #取得串列索引start到最後
    mylist[-n:] #取得串列後n名
    mylist[:] #取得所有元素

    mylist[start:end:step] #每隔stpe，讀取索引start到end-1索引的串列元素

'''

# Ch6_04.py 列出特定區間球員的得分子串列
james = [23, 19, 22, 31, 18]
print("列印james第1-3場得分: ", james[0:3])
print("列印james第2-4場得分: ", james[1:-1])
print("列印james第1, 3, 5場得分: ", james[0::2])

# Ch6_05.py 列出球隊前3名隊員、從索引1到最後隊員與後3名隊員子串列
players = ['curry', 'durant', 'iquodala', 'john cena', 'thompson', 'bell']
first3 = players[:3]
print('前三名球員', first3)
n_to_last = players[1:]
print('球員索引1到最後', n_to_last)
last3 = players[-3:]
print('最後三名球員', last3)

# Ch6_6.py 串列索引值是-1代表是最後一個串列元素。
players = ['curry', 'durant', 'iquodala', 'john cena', 'thompson', 'bell']
print('最後一位球員', players[-1])
james = [23, 19, 22, 31, 18]
print('james最後一場分數', james[-1])
mixs = [1, 3, 'hello']
print('mix最後一個元素', mixs[-1])

# Ch6_7.py 使用負索引列出索引串列內容
players = ['curry', 'durant', 'iquodala', 'john cena', 'thompson', 'bell']
print(players[-1], players[-2], players[-3], players[-4], players[-5])
