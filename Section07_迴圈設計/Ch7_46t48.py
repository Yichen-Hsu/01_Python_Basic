'''
設計真實的成績系統排序

要處理成績系統，關鍵是學會使用而為串列的排序，如果想針對串列內第n個元素值排序，使用方法如下:

二維串列.sort(key=lambda x:x[n]) 
 
'''
# Ch7_46.py

sc = [
    [1, '海綿寶寶', 80, 95, 88, 0, 0, 0],
    [2, '天線寶寶', 98, 97, 93, 0, 0, 0],
    [3, '彩虹寶寶', 91, 93, 92, 0, 0, 0],
    [4, '豆豆先生', 92, 97, 92, 0, 0, 0],
    [5, '鯊魚寶寶', 94, 94, 82, 0, 0, 0],
]
# 計算總分與平均
print('填入總分與平均')
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])
    sc[i][6] = round(sc[i][5] / 3, 1)
    print(sc[i])
sc.sort(key=lambda x:x[5], reverse=True)
# 以下填入名次
print('填入名次')
for i in range(len(sc)):
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x:x[0])
print('最後成績單')
for i in range(len(sc)):
    print(sc[i])


'''
上述成績系同仍不完美，如果發生2個人的成績相同時，座號屬於後面的人名次將往下掉一名
'''

#Ch7_47.py 修改Ch7_46
sc = [
    [1, '海綿寶寶', 80, 95, 88, 0, 0, 0],
    [2, '天線寶寶', 98, 97, 93, 0, 0, 0],
    [3, '彩虹寶寶', 91, 93, 92, 0, 0, 0],
    [4, '豆豆先生', 92, 97, 92, 0, 0, 0],
    [5, '鯊魚寶寶', 94, 94, 88, 0, 0, 0],
]
# 計算總分與平均
print('填入總分與平均')
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])
    sc[i][6] = round(sc[i][5] / 3, 1)
    print(sc[i])
sc.sort(key=lambda x:x[5], reverse=True)
# 以下填入名次
print('填入名次')
for i in range(len(sc)):
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x:x[0])
print('最後成績單')
for i in range(len(sc)):
    print(sc[i])


# Ch7_48.py 計算圓周率

'''
使用布萊尼茲公式

pi = 4 * (1 - 1/3 + 1/5 - 1/7 + (-1)**i+1/2i-1)
'''

x = 1000000
pi = 0
for i in range(1, x+1):
    pi += 4 * ((-1)**(i+1)/(2*i-1))
    if i % 100000 == 0:
        print(f'當{i = : 7d} 時 PI = {pi:20.19f}')