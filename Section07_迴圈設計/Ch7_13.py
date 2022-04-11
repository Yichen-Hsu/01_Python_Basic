'''
有三個參數的range()函數

當range()函數搭配三個參數時，它的語法格式如下:

range(start, end, step)
'''

# Ch7_13.py 輸入一個正整數n，這個程式會列出從1加到n的總和
n = int(input("請輸入整數: "))
total = sum(range(n+1))
print(f"從1到{n}的總和是 = {total}")

