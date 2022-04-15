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


'''
串列生成(generator)是一種使用迭代方式產生Python數據資料的方式，例如:可以產生串列、字典、集合等。
這是結合迴圈與條件運算式的精簡程式碼的方法
'''
# Ch7_15_2.py 最初讀者可能會用的方式增加串列元素

xlist = []
xlist.append(0)
xlist.append(1)
xlist.append(2)
xlist.append(3)
xlist.append(4)
xlist.append(5)
print(xlist)

# Ch7_15_3.py 使用for迴圈重新設計

xlist = []
for i in range(6):
    xlist.append(i)
print(xlist)

# Ch7_15_4.py 直接使用list()將range(n)當作是參數，重新設計上述程式。
xlist = list(range(6))
print(xlist)

# Ch7_15_5.py 使用串列生程式產生串列。
xlist = [n for n in range(6)]
print(xlist)