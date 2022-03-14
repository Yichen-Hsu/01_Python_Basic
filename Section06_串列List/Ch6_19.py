'''
如果想建立一個串列，可以暫時不放置元素，可使用下列方式宣告。

mylist = []  #這是空的串列

'''

# Ch6_19.py 刪除串列元素的應用，這個程式基本上會用len()函數判斷串列內是否有元素資料，如果有刪除索引為0的元素，如果沒有則列出串列內沒有元素了。

cars = ['toyota', 'honda', 'food panda']
print(f"cars串列長度是 = {len(cars)}")
if len(cars) != 0:
    del cars[0]
    print("刪除cars串列元素成功")
    print(f"cars串列長度是={len(cars)}")
else:
    print("cars串列內沒有元素資料")
nums = []
print(f"nums串列長度是 = {len(nums)}")
if len(nums):
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列元素內沒有元素資料")

'''
python 也允許我們刪除整個串列，串列經過一整個刪除後就無法復原，同時也無法做任何操作了，下列是刪除串列的方式

del mylist  #刪除串列mylist
'''

# 建立串列、列印串列、刪除串列，然後嘗試再度列印串列結果出現錯誤訊息，因為串列經刪除後已經不存在了。

'''
x = [1, 2, 3]
del x
print(x) #此行則會跳出錯誤訊息
'''

'''
補充多重指定與串列

在多重指定中，如果等號左邊的變數較少，可以用 "*變數" 方式，將多餘的右邊內容用串列方式打包含 "*" 的變數。
'''
# ex1: 將多的內容打包給c
a, b, *c = 1, 2, 3, 4, 5, 6
print(a, b, c)
# ex2: 將多的內容打包給b
a, *b, c = 1, 2, 3, 4, 5
print(a, b, c)