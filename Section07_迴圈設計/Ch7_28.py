'''
for...else 迴圈

在設計for迴圈時，如果期待所有的if敘述條件是False時，在最後一次迴圈後，可以執行特定程式區塊指令，可使用這個敘述，這個指令通常是和if和break敘述配合使用。
下列是常用的語法格式:

for var in 可迭代物件:
    if 條件運算式:
        程式區塊碼 1
        break
else:
    程式碼區塊2
'''

# Ch7_28.py 質數測試的程式，如果所輸入的數字是質數則列出式質數，否則列出不是質數。
num = int(input("請輸入大於1的整數做質數測試: "))
if num <= 1:
    print("請重新啟動程式")
elif num == 2:
    print(f"{num}是質數")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num}不是質數")
            break
    else:
        print(f"{num}是質數")

'''
質數的英文式 Prime number
'''