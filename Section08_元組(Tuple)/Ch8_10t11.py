'''
串列與元組資料互換

程式設計過程中也會有需要將其他資料行帶轉換成串列與元組，或是串列與元組資料型態互換，可使用下列指令:

list(data): 將元組或其他資料型態改為串列
tuple(data): 將串列或其他資料型態改為員組

'''

# Ch8_10.py 將元組改為串列的測試。
keys = ('maagic', 'xaab', 9099)
list_keys = list(keys)
list_keys.append('secret')
print(f'列印元組 {keys}')
print(f'列印串列 {list_keys}')


# Ch8_11.py 將串列改為員組的測試。

keys = ['maagic', 'xaab', 9099]
tuple_keys = tuple(keys)
print(f'列印串列 {keys}')
print(f'列印元組 {tuple_keys}')
tuple_keys.append('secret')
