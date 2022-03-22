'''
刪除指定的元素remove()

在刪除串列元素時，有時可能不知道元素在串列內的位置，此時可以使用remove()方法刪除指定的元素

mylist.remove(想刪除的元素內容)

如果串列內有相同的元素，則只刪除第一個出現的元素，如果想要刪除所有相同的元素，必須使用迴圈。
'''

# Ch6_27.py
names = ['Ding Ding', 'Dici', 'Lala', 'Hsiao Po']
print("目前串列內容 = ", names)
print("使用 remove() 刪除串列元素")
byebye = 'Ding Ding'
names.remove(byebye)
print(f'所刪除的內容是: {byebye} 而沒有為什麼')
print(f'新的串列內容是: {names}') 