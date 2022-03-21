'''
刪除串列元素pop()

使用pop()方法刪除元素的優點是，刪除後將傳回所刪除的值，使用pop()時，若是未指定刪除元素的位置，一律刪除串列末端的元素
'''

# Ch6_26.py 使用pop()刪除串列元素的應用
nums = [1, 2, 3, 4, 5]
print("使用pop()刪除串列元素: ")
popped_num = nums.pop()
print("所刪除的元素是", popped_num)
print("新的串列內容 = ", nums)
print("-" * 30)
nums = [1, 2, 3, 4, 5]
print("使用pop(1)刪除串列元素")
popped_num = nums.pop(1)
print("所刪除的元素是", popped_num)
print("新的串列內容 = ", nums)

