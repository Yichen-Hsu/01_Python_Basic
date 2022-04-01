'''
in 和 not in 運算式

主要用於判斷一個物件是否屬於另一個物件，物件可以是字串(string)、串列(list)、元組(Tuple)、字典(Dict)。

bool_value = obj1 in obj2  若obj1在物件obj2內物件會回傳True
bool_value = obj1 not in obj2  若obj1不在物件obj2內物件會回傳True
'''

obj1 = 'c'
obj2 = 'claender'
x = obj1 in obj2
print(x)

# Ch6_51.py 請輸入字元，這個程式會判斷字元是否在字串內。
password = 'helloworld'
ch = input('請輸入字元: ')
print("in 運算式")
if ch in password:
    print("輸入字元在密碼中")
else:
    print("輸入字元不在密碼中")
print("not in 運算式")
if ch not in password:
    print("輸入字元在密碼中")
else:
    print("輸入字元不在密碼中")

'''
此功能常用在偵測某筆元素是否存在串列中，如果不存在，則將它加入串列內
'''

fruits_list = ['apple', 'banana', 'pineapple']
fruit = input("請輸入水果名稱: ")
if fruit in fruits_list:
    print("此水果已經存在")
else:
    fruits_list.append(fruit)
    print(f"已經為您添加新的水果 {fruit} 進入列表中")
    print(fruits_list)