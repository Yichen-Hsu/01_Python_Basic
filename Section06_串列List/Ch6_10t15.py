'''
程式設計時，可能會增加元素，也可能會刪除元素
時間久了即使是當時的程式設計者也將無法得知串列內元素剩餘多少
因此會使用 len() 函數查詢串列內部有多少元素
'''
# Ch6_10.py 使用len()函數
james = [23, 19, 22, 31, 18] 
games = len(james)
print(f"經過{games}場次比賽，James單場得分最高為{max(james)}, 單場最低分為{min(james)}, 總得分為{sum(james)}")

# Ch6_11.py 更改串列元素內容，修改James第五場比賽分數
james = [23, 19, 22, 31, 18] 
print(f"舊的James比賽分數{james}")
james[4] = 28
print(f"新的James比賽分數{james}")

# Ch6_12.py 
cars = ['Nissan', 'Ford', 'Toyota']
print(cars)
cars[1] = 'Honda'
print(cars)

'''
串列相加: Python 是允許 "+"和"+="執行串列相加，相當於將串列結合。
'''

# Ch6_13.py
cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['bmw', 'audi']
cars1 += cars2
print('品牌串列', cars1)

# Ch6_14.py
num1 = [1, 3, 5]
num2 = [2, 4, 6]
num3 = num1 + num2
print(num3)

# Ch6_15.py 如果將串列乘以一數字，相當於是串列元素重複次數。
cars = ['toyota', 'Nissan', 'Lexus']
nums = [1, 3, 5]
multiple_cars = cars * 5
print(multiple_cars)
numlist = nums * 3
print(numlist)
