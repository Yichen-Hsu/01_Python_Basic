'''
while迴圈暫時停止不往下執行 - continue指令

在設計while迴圈時，如果期待某些條件發生時可以往下執行迴圈內容，此時可以用continue指令，這個指令通常是和if敘述配合使用。
下列是常用的語法格式:

while條件運算式A:
    程式區塊碼1
    if 條件運算式 B: 
        程式區塊碼2
        continue
    程式區塊碼3
'''

# Ch7_38.py 列出1至10之間的偶數
index = 0
while index <=10 :
    index += 1
    if index %2:
        continue
    print(index)

'''
while迴圈條件算是與可迭代物件
'''

# Ch7_39.py 刪除串列內的apple字串，程式第五行，只要在fruits串列內可以找到變數fruit內容是apple, 就回傳True, 迴圈將繼續
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']
fruit = 'apple'
print('刪除前的fruits = ', fruits)
while fruit in fruits:
    fruits.remove(fruit)
print('刪除後的fruits = ', fruits)


# Ch7_40.py 有一個串列buyers，此串列內含購買者和消費金額，如果購買金額超過或達到1000元，則歸類為VIP買家vipbuers串列。否則是Gold買家goldbuyers串列。

buyers = [
    ['James', 1030], ['Curry', 893], ['Durant', 2020], ['Jordan', 1059], ['David', 496], ['Tony', 250]
]

goldbuyers = []
vipbuyers = []

while buyers:
    index_buyers = buyers.pop()
    if index_buyers[1] >= 1000:
        vipbuyers.append(index_buyers)
    else:
        goldbuyers.append(index_buyers)
print('vip買家資料分別為: ', vipbuyers)
print('gold買家資料分別為: ', goldbuyers)
