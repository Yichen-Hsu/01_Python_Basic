'''
建立一個空字典

在程式設計時，也允許建立一個空字典，建立空字典的語法如下:
mydict = {}
上述建立完成後，可以用9-1-3節增加字典元素的方式為空字典建立元素。
'''

# Ch9_12.py 建立一個小兵的空字典，然後為小兵建立元素
soldier0 = {}
print('空小兵的字典', soldier0)
soldier0['tag'] = 'red'
soldier0['score'] = 3
print('新的小兵字典', soldier0)