'''
for迴圈暫時停止不往下執行 - continue指令
'''

# Ch7_26.py 有一個串列scores紀錄James的比賽得分，設計一個程式可以列出James有多少場次得分大於或等於3o分。
scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
score = []
for i in range(len(scores)):
    if scores[i] >= 30:
        score.append(scores[i])
        continue
print(score)
print(f'James得分超過30分場數總共有{len(score)}場')

# Ch7_27.py 有一個串列players, 這個串列的元素也是串列，包含球員名字和身高資料，列出所有身高是200公分(含以上)的球員資料
players = [['James', 202], ['Curry', 193], ['Durant', 205], ['Jordan', 199], ['David', 211]]
answer = []
for i in range(len(players)):
    if players[i][1] >= 200:
        answer.append(players[i])
        continue
print(answer)
