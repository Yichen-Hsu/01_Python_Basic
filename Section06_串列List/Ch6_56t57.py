'''
enumerate 物件

enumerate() 可以將迭代類(iterable)數值的元素用索引值與元素配對的方式傳回，返回的數據稱enumerate物件。
這個方式可以為可迭代物件的每個元素增加索引值，這對未來的數據應用是有幫助的。
其中可迭代類的數值可以是串列(list)、元祖(Tuple)、集合(Set)等。 

obj = enumerate(iterable, start=0) #若省略start設定的定義，預設索引值是0
'''

# Ch6_56.py 將資料轉成enumerate物件，同時列出此物件類型 
drinks = ["coffee", 'tea', 'wine']
enumerate_drinks = enumerate(drinks)
print(enumerate_drinks)
print('下列是輸出enumerate物件類型')
print(type(enumerate_drinks))

# Ch6_57.py 將資料轉成enumerate物件，再將enumerate物件轉成串列的實例，start索引值起始分別是0和10
drinks = ['coffee', 'tea', 'vodka']
enumerate_drinks = enumerate(drinks)
print('轉成串列輸出，初始索引值是 0 = ', list(enumerate_drinks))
enumerate_drinks = enumerate(drinks, start=10)
print('轉成串列輸出，初始索引值是 10 = ', list(enumerate_drinks))
