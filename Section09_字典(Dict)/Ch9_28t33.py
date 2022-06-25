'''
字典常用的函數和方法
'''

# Ch9_28.py 列出字典以及字典內的字典元素個數。

wechat_account = {
    'helloworld':{
        'last name':'Hsu',
        'first name':'Ey',
        'city':'Maioli'
    },
    'kevin':{
        'last name':'ken',
        'first name':'ni',
        'city':'one'
    }
}

print('wechat_account 字典元素個數: ', len(wechat_account))
print('wechat_account[helloworld] 字典元素個數: ', len(wechat_account['helloworld']))
print('wechat_account[kevin] 字典元素個數: ', len(wechat_account['kevin']))

'''
fromkeys()

這是建立一個字典的方法，它的語法格式如下:

mydict = dict.fromkeys(seql[, value])

上述會使用seq序列建立字典，序列內容將是字典的鍵，如果沒有設定value則用none當字典的值
'''

# Ch9_29.py 分別使用串列和元組建立字典。
# 將串列轉成字典
seq1 = ['name', 'city']
list_dict1 = dict.fromkeys(seq1)
print(f'字典1{list_dict1}')
list_dict2 = dict.fromkeys(seq1, 'Chicago')
print(f'字典2{list_dict2}')
# 將元組轉成字典
seq2 = ('name', 'city')
list_dict1 = dict.fromkeys(seq2)
print(f'字典1{list_dict1}')
list_dict2 = dict.fromkeys(seq2, 'New York')
print(f'字典2{list_dict2}')

'''
get()

搜尋字典的鍵，如果鍵存在則傳回該鍵的值，如果不存在則傳回預設值。

ret_value = mydict.gt(key[, default=none])

key 是要搜尋的鍵，如果找不到key則傳回default的值(如果沒設default值就傳回none)

'''

# Ch9_30.py get()方法的應用
fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print('Value = ', ret_value1)
ret_value2 = fruits.get('grape')
print('Value = ', ret_value2)
ret_value3 = fruits.get('grape', 10)
print('Value = ', ret_value3)



'''
setdefault()

這個方法基本上與get相同，不同之處在於get()方法不會改變字典內容。使用setdefault()方法時若所搜尋的鍵不在
會將"鍵:值"加入字典，如果有設定預設值則將鍵:預設值加入字典，如果沒有設定預設值則將鍵:None加入字典

ret_value = mydict.setdefault(key[, default=none]) #mydict 是欲搜尋的字典

'''

# Ch9_30_1.py setdefault()方法，鍵在字典內的應用
# key在字典內
fruits = {'Apple':20, "Orange":25}
ret_value = fruits.setdefault('Orange')
print('value = ', ret_value)
print('fruits字典', fruits)
ret_value = fruits.setdefault('Orange')
print('value = ', ret_value)
print('fruits字典', fruits)

# Ch9_30_2.py setdefault()方法，鍵不在字典內的應用。
person = {'name':'John'}
print('原先字典內容', person)

# age鍵不存在
age =person.setdefault('age')
print('增加age鍵', person)
print('age = ', age)

# sex鍵不存在
sex = person.setdefault('gender', 'Male')
print('增加gender鍵', person)
print('gender = ', sex)

'''
有時我們想要製作更大型的字典資料結構，例如: 字典的鍵是地球的洲名，鍵的值是該洲的名稱，可以參考以下實例。
'''

# ex1 字典的元素的值是串列

asia = {'Beijing', 'Hongkong', 'Tokyo'}
usa = {'Chicago', 'New York', 'Hawaii', 'Los Angeles'}
europe = {'Paris', 'London', 'Zurich'}
world = {'Asia': asia, 'USA':usa, 'Europe':europe}
type(world)
print(world)

'''
在設計大型程式時，必須記住字典的鍵是不可變的，所以不可以將串列、字典或是下一章將介紹的集合當作字典的鍵，不過可以將元組當作字典的鍵
例如:我們在4-7-4節可以知道地球每個位置是用(經度, 緯度)當作標記，所以我們可以使用經緯度當作字典的鍵。
'''

# ex2 使用經緯度當作字典的鍵，值是地點名稱。
loc = {
    (25.0452, 121.5168):'台北車站',
    (22.2838, 114.1731):'紅磡車站'
}
type(loc)
print(loc)

'''
傳統方式分析文章的文字與字數
'''

# Ch9_31.py 這個專案主要是設計一個程式，可以記錄一段英文字，或是一篇文章所有單字以及每隔單字的出現次數，這個程式會用單字當作字典的鍵(key)，用值(value)當作該單字出現的次數。

song = '''Are you sleeping, are you sleeping. Brother John, Brother John?
Morning bells are ringing morning bells are ringing.
Ding ding ding, Ding ding ding
'''
mydict = {}
print('原始歌曲')
print(song)

# 以下是將歌曲大寫字母勸都改成小寫
songlower = song.lower()
print('小寫歌曲')
print(songlower)

# 將歌曲的標點符號用空字元取代
for ch in songlower:
    if ch in ".,?":
        songlower = songlower.replace(ch, '')
print('不再有標點符號的歌曲')
print(songlower)

# 將歌曲字串轉成串列
songlist = songlower.split()
print('以下是歌曲串列')
print(songlist)

# 將歌曲串列處理成字典
for wd in songlist:
    if wd in mydict:
        mydict[wd] += 1
    else:
        mydict[wd] = 1

print('以下是執行結果')
print(mydict)

'''
字典生成式

新字典 = {鍵運算式:值運算式 for 運算式 in 可迭代物件}
'''
# Ch9_32.py 使用字典生成式紀錄單字deepstone, 每個字母出現的次數
word = 'deepstone'
alphabetCount = {alphabet:word.count(alphabet) for alphabet in word}
print(alphabetCount)

'''
上述程式的執行原理是將每個單字出現的次數當作是鍵的值，當然如果硬要挑起上述程式的缺點，就在對於字母e而言，在for迴圈中會被執行3次。

當了解Ch9_32.py後若是再看Ch9_31.py這個程式的重點是將串列改為字典同時計算每個單字出現的次數
'''

# Ch9_33.py 使用串列生成方式重新設計Ch9_31.py
mydict = {wd:songlist.count(wd) for wd in songlist}
print(mydict)