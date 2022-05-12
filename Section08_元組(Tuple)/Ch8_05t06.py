'''
全新定義方式修改元組元素
'''
# Ch8_5.py 用重新定義方式修改元組元素內容。

fruits = ('apple', 'orange')
print('原始fruits元組元素')
for fruit in fruits:
    print(fruit)

fruits = ('watermelon', 'grape')
print('\n新的fruits元組元素')
for fruit in fruits:
    print(fruit)

'''
元組切片(tuple slices)
'''
# Ch8_6.py 元組切片的應用
fruits = ('apple', 'orange', 'banana', 'watermelon', 'grape')
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
print(fruits[-2:])
print(fruits[0:5:2])
