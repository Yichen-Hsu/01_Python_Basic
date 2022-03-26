'''
串列賦值

定義一個串列，再使一參數被賦予其定義的串列

ex.
my_num = [1, 2, 3, 4, 5, 6]
new_num = my_num
'''
# Ch6_41.py 列出我和朋友所喜歡的共同運動
mysport = ['tennis', 'boarding sport']
myfriendsport = mysport
print('我喜歡的運動', mysport)
print('我朋友喜歡的運動', myfriendsport)



'''
注意，只要有一格串列更改元素，就會影響到另一個串列同步更改，這是「賦值」的特性，所以使用上要小心。
'''

# Ch6_42.py
mysport = ['tennis', 'boarding sport']
myfriendsport = mysport
print('我喜歡的運動', mysport)
print('我朋友喜歡的運動', myfriendsport)
mysport.append('archering')
myfriendsport.append('moutain climbing')
print('我喜歡的運動_改', mysport)
print('我朋友喜歡的運動_改', myfriendsport)
