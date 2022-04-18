# Ch7_20.py 簡化Ch7_19,py程式，然後列出串列內每個元素串列值。

colors = ['red', 'green', 'blue']
shapes = ['circle', 'square']
result = [[color, shape] for color in colors for shape in shapes]
for color, shape in result:
    print(color, shape)
for i in range(len(result)):
    print(result[i])
for shape in result:
    print(color)

'''
含有條件式的串列生成

新串列 = [運算式 for 項目 in 可迭代物件 if 條件式]
'''
# ex.
new_list = [n for n in range(1, 11) if n%2 != 0]
print(new_list)

'''
列出ASCII碼值或Unicode碼值的字元
'''
for x  in range(32, 128):
    print(chr(x), end=' ')

for x in range(0x6d2a, 0x6e2a):
    print(chr(x), end=' ')
print()
'''
進階的for迴圈應用

巢狀for迴圈
一個回圈內還有另一個迴圈
'''

# Ch7_21.py 列印一個9*9乘法表
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f'{i} * {j} = {result:<3d}', end='    ')
    print()
