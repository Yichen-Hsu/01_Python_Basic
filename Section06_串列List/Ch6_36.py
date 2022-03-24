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

