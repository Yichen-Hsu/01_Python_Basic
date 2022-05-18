'''
生成式(generator)

num = (n for n in range(6))

並不會產生元組生成式，而是產生生成式(generator)物件，這是一個可迭代物件，你可以用迭代方式取出內容，也可以用list()將生成式變為串列。
或是用tuple變為元組，但是只能使用一次，因為這個生成式不會記住所有擁有的內容，如果使用第二次，將得到空串列
'''

x = (n for n in range(6))
print(type(x))
for n in x:
    print(n)

x = (n for n in range(6))
xlst = list(x)
print(xlst)
xtup = tuple(x)
print(xtup)

'''
製作大型的元組資料
'''

# 元組的元素是串列
asia = ['Beijin', 'Hongkong', 'Tokyo']
europe = ['Germany', 'France', 'Italy']
north_america = ['Canada', 'USA']
world = asia, europe, north_america
print(type(world))
print(world)

'''
元組的功能

1. 可以更安全的保護資料
程式設計時可能會碰上有些資料是永遠不會被改變的事實，將它儲存在元組內，可以安全的被保護
例如: 影像處理時物件的長、寬或每一像素的色彩資料，很多都是以元組的資料型態


2. 增加程式執行的速度
元組結構比串列簡單，占用較少的系統資源，程式執行時速度比較快。
'''

'''
認識元組

元組具有安全、內容不會被竄改、資料結構單純、執行速度快等優點，
所以其實被大量應用在系統程式設技師，程式設計師喜歡將程式設計所保留的資料以元組儲存。

divmod() 函數的回傳值是商和餘數(元組型態)

商, 餘數 = divmod(被除數, 除數)
'''

# Ch8_19.py 計算地球到月球的時間
dist = 384400
speed = 1225
total_hours = dist // speed
data = divmod(total_hours, 24)
print('divmod傳回的資料型態是: ', type(data))
print(f'總共需要{data[0]}天')
print(f'{data[1]} 小時')