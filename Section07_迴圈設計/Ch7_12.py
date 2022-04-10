'''
有兩個參數的range()函數

當range()函數搭配2個參數時，語法如下:
range(start, end)  #start是起始值，end-1是終止值。

如果終止值小於起始值則產生 空序列 或稱 空range物件
'''

# ex. 終止值小於起始值，不會印出任何東西
for i in range(10, 2):
    print(i)

# Ch7_12.py 輸入正整數n值，這個程式會從0加到n之值
n = int(input("請輸入n值: "))
sum = 0
for num in range(1, n+1):
    sum += num
print("總和 = ", sum)