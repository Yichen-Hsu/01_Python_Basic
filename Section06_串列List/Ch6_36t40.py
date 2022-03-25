'''
串列內含串列

num = [1, 2, 3, 4, 5, [6, 7, 8]]

如果想要存取串列內的串列元素，可以使用下列格式:
num[索引1][索引2]

索引1 是元素串列原先索引位置
索引2 是元素串列內部的索引

'''
# example.
from turtle import position


num = [1, 2, 3, 4, 5, [6, 7, 8]]
print(num[5][0])
print(num[5][1])
print(num[5][2])

# Ch6_36.py 
James = [['Lebron James', 'SF', '12/30/84'], 23, 19, 22, 31, 18] #定義James串列
games = len(James)
score_Max = max(James[1:games])
i = James.index(score_Max)
name = James[0][0]
postion = James[0][1]
birth = James[0][2]
print(f'姓名: {name}')
print(f'位置: {position}')
print(f'出生日期: {birth}')
print(f'在第 {i} 場得分最高 {score_Max}')

# Ch6_37.py 發揮 Python 精神
James = [['Lebron James', 'SF', '12/30/84'], 23, 19, 22, 31, 18] #定義James串列
games = len(James)
score_Max = max(James[1:games])
i = James.index(score_Max)
name, position, birth = James[0]
print(f'姓名: {name}')
print(f'位置: {position}')
print(f'出生日期: {birth}')
print(f'在第 {i} 場得分最高 {score_Max}')

'''
也可以使用append()函數將某一串列插入另一串列的末端
'''

# Ch6_38.py 使用append()將串列插入另一串列的末端
cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['BMW', 'ford']
print('原先cars1串列內容: ', cars1)
print('原先cars2串列內容: ', cars2)
cars1.append(cars2)
print(f'執行append()後串列cars1內容 = {cars1}')


'''
extend() 會將串列分解成元素，一一插入被extend的串列。
使用格式如下:

串列A.extend(串列B)
'''

# Ch6_39.py 
A = ['Hello', 'World', "How"]
B = ['Are', 'You']
A.extend(B)
print(f'執行extend()之後的A: {A}')

'''
二為串列(two dimension list)
'''

# Ch6_40.py 使用二維串列的成績系統總分計算。
sc = [
    ['Ethan', 59, 69, 79, 0],
    ['Cathy', 60, 70, 49, 0]
]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
print(sc[0])
print(sc[1])
