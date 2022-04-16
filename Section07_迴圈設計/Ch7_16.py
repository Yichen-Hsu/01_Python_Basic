# Ch7_16.py 重新設計Ch7_15.py, 進階串列生成的應用。
n = int(input("請輸入整數: "))
if n > 19 : n = 10
squares = [ num ** 2 for num in range (1, n+1)]
print(squares)