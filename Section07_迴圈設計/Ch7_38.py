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