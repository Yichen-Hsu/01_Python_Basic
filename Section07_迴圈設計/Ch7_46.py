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
