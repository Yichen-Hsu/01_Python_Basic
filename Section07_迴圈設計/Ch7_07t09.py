'''
將for迴圈應用在資料類別的判斷
'''

# Ch7_07.py 有一個flies串列內容一系列檔案名稱，請將".py"的python程式檔案另外建立到py串列，然後列印。
files = ['day1.c', 'day2.py', 'day3.py', 'day4.java']
py = []
for file in files:
    if file.endswith('.py'):
        py.append(file)
print(py)

# Ch7_08.py 有一個串列names，元素內容是姓名，請將姓洪的成員建立在lastname串列內，然後列印。
names = ['金城武', '孫東寶', '周星馳', '吳孟達', '吳少強']
lastname = []
for name in names:
    if name.startswith('吳'):
        lastname.append(name)
print(lastname)

# Ch7_09.py 刪除串列fruits2內在fruits1內已有的元素，我們可以使用for迴圈完成此工作。
fruits1 = ['apple', 'banana', 'water melon', 'peach', 'passionfruit']
fruits2 = ['banana', 'guava', 'water melon']
print('目前fruits2串列: ', fruits2)
for fruits in fruits2[:]:
    if fruits in fruits1:
        fruits2.remove(fruits)
        print(f'刪除 {fruits}')
print('最後fruits2串列: ', fruits2)