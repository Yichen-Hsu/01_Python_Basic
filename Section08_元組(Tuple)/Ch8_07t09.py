'''
方法與函數

應用在串列上的方法或函數如果不會更改元組內容, 則可以將它應用在原祖, 例如: len()
'''

# ch8_07.py 列出元祖元素長度
keys = ('magic', 'xaab', 9909)
print(f'keys元祖的長度是{keys}')


# Ch8_08.py 誤用會減少元祖元素的方法pop(), 產生的錯誤實例
keys = ('magic', 'xaab', 9909)
key = keys.pop()

# Ch8_09.py 誤用會增加原組元素的方法append(), 產生的錯誤實例
keys = ('magic', 'xaab', 9909)
key = keys.append('secret')