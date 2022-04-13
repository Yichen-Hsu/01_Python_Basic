'''
有三個參數的range()函數

當range()函數搭配三個參數時，它的語法格式如下:

range(start, end, step)
'''

# Ch7_13.py 輸入一個正整數n，這個程式會列出從1加到n的總和
# n = int(input("請輸入整數: "))
# total = sum(range(n+1))
# print(f"從1到{n}的總和是 = {total}")

# Ch7_14.py 建立一個整數平方的串列，為了避免數值太大，若是輸入大於10，此大於10的數值將被設為10
# squares = []
# n = eval(input("請輸入整數: "))
# if n > 10: n = 10
# for num in range(1, n+1):
#     value = num * num
#     squares.append(value)
# print(squares)

# Ch7_15.py 
# squares = []
# n = int(input("請輸入整數: "))
# if n > 10: n = 10
# for num in range(1, n+1):
#     squares.append(num**2)
# print(squares)

# Ch7_15_1.py 刪除串列內所有元素，Python沒有提供刪除整個串列元素的方法，不過我們可以使用for迴圈完成此工作。
fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print("目前fruits串列: ", fruits)
for fruit in fruits[:]:
    fruits.remove(fruit)
    print(f'刪除 {fruit}')
    print('目前fruits串列: ', fruits)