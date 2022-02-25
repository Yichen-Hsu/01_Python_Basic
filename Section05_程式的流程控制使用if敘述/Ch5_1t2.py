'''
關係運算子如下:
> 大於, >= 大於等於, < 小於, <= 小於等於, == 等於, != 不等於

邏輯運算子:
and, or, not
'''

# Ch5_1.py if敘述的基本應用
age = input("請輸入年齡: ")
if (int(age)) < 20:
    print("你還太年輕")
    print("需要滿20歲才可以購買菸酒")

# Ch5_2.py 輸出絕對值的應用
print("輸出絕對值")
num = input("請輸入任一整數: ")
x = int(num)
if (int(x) < 0): x = -x
print(f"絕對值是{x}")
