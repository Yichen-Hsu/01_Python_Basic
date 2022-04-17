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