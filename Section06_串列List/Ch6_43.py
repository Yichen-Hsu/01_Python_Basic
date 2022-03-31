'''
位址的觀念

對於串列而言，如果使用下列方式設定2個串列變數相等，相當於只是將變數位址拷貝給另一個變數。

hello1 = hello2

而因為兩個變數所指的位址相同，所以新增項目時，兩個串列的內容將同步更改。
'''
# Ch6_43.py
hello1 = [1, 2, 3, 4 ,5]
hello2 = hello1
print(f'列出hello1的位址: ', id(hello1))
print(f'列出hello2的位址: ', id(hello2))
print('hello1的值為: ', hello1)
print('hello2的值為: ', hello2)
hello1.append(10)
hello2.append(11)
print('-----新增項目後-------')
print(f'列出hello1的位址: ', id(hello1))
print(f'列出hello2的位址: ', id(hello2))
print('hello1的值為: ', hello1)
print('hello2的值為: ', hello2)

