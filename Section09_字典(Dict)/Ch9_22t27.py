'''
建立字典串列

讀者可以思考一下程式實例Ch9_2.py，我們建立了小兵soldier0字典，在真實的遊戲設計中為了讓玩家展現雄風，玩家將面對數十、數百或更多個小兵所組成的敵軍
為了管理這些小兵，可以將每個小兵當作一個字典，字典內則有小兵的各種資訊，然後將這些小兵字典放入串列內。
'''
# Ch9_22.py 建立三個小兵字典，然後將小兵組成串列(list)
soldier0 = {'tag':'red', 'score':3, 'speed':'slow'}
soldier1 = {'tag':'green', 'score':5, 'speed':'medium'}
soldier2 = {'tag':'blue', 'score':10, 'speed':'fast'}
armys = [soldier0, soldier1, soldier2]
for army in armys:
    print(army)



'''
程式設計如果每個小兵皆要個別設計這樣太沒效率了，我們可以使用7-2節的range()函數處理這類問題。
'''

# Ch9_23.py 使用range()建立50個小兵，tag是red、score是3、speed是slow
armys = []
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
for solider in armys[:3]:
    print(soldier)
print('小兵數量 = ', len(armys)) 

'''
對python而言，雖然50個特徵相同的小兵放在串列內，其實每個小兵皆是獨立，可用索引方式存取。通常可以在遊戲過程中使用if敘述和for迴圈處理。
'''

# Ch9_24.py 重新設計Ch9_23.py建立50個小兵，但是將編號第36到38名的小兵改成tag是blue、score是5、speed是medium
armys = []
armys = []
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
print('列印前3個小兵')
for solider in armys[:3]:
    print(soldier)
print('小兵數量 = ', len(armys)) 
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'blue'
        soldier['score'] - 5
        soldier['speed'] = 'meduim'
# 列印編號35到40小兵資料
print('列印編號35到40小兵資料')
for soldier in armys[34:40]:
    print(soldier)



'''
字典內鍵的值是串列

在python的應用中也允許將串列放在字典內，這時串列將是字典某鍵的值。
如果想要遍歷這類資料結構，需要使用巢狀迴圈和字典的方法items(), 外層迴圈是取得字典的鍵,
內層迴圈是將含串列的值拆解。下列是定義sports字典的實例:

sports = {
    'Curry' : ['籃球', '美式足球']
    'Durrant' : ['棒球']
    'James' : ['美式足球', '棒球', '籃球']
}

上述sports字典內含有3個"鍵:值"配對元素，其中值的部分皆是串列。程式設計時外層迴圈配合items()方法，設計如下:

for name, favorite_sport in sports.items():
    print('%s 喜歡的運動是: ' % name)

上述設計後，鍵內容會傳給name變數，值內容會傳給favorite_sport變數，所以將可以列印鍵內容
內層迴圈主要是將favorite_sport串列內容拆解，它的設計如下:

for sport in favorite_sport:
    print(' ', sport)

上述串列內容會隨迴圈傳給sport變數，所以可以列出結果。
'''

# Ch9_25.py 字典內含串列元素的應用，本程式會先定義內含字串的字典，然後再拆解列印。

sports = {
    'Curry' : ['籃球', '美式足球'],
    'urrant' : ['棒球'],
    'James' : ['美式足球', '棒球', '籃球']
}
for name, favorite_sport in sports.items():
    print(f'{name} 喜歡的運動是: ')
    for sport in favorite_sport:
        print(' ', sport) 


'''
在Python的應用中也允許將字典放在字典內，這時字典將是字典某鍵的值。
假設微信(wechat_account)的帳號是用字典儲存，鍵有兩個值是由另外字典組成，這個內部字典另有3個鍵
分別是last_name、first_name和city，下列是設計實例。
'''

# Ch9_26.py 列出字典內含字典的內容
wechat_account = {
    'cshung':{
        'last name':'Hsu',
        'first name':'Ey',
        'city':'Taipei'
    },
    'Kevin':{
        'last name':'Lee',
        'first name':'Pon',
        'city':'Taipei'
    }
}
for account, account_info in wechat_account.items():
    print('使用者帳號 = ', account)
    name = account_info['last name'] + ' ' + account_info['first name']
    print('姓名: ', name)
    print('城市: ', account_info['city'])

'''
while迴圈在字典的應用
'''

# Ch9_27.py 這是一個市場夢幻旅遊地點調查的實例，此程式會要求輸入名字以及夢幻旅遊地點，然後存入survey_dict字典其中鍵是name, 值是travel_location
# 輸入完後程式會詢問是否有人要輸入，y表示有, n表示沒有則程式結束，程式結束前會輸出市場調查結果。

survey_dict = {}       #建立市場調查空字典
market_survey = True   #設定迴圈布林值

# 讀取參加市場調查者姓名和夢幻旅遊景點
while market_survey:
    name = input('\n請輸入姓名: ')
    travel_location = input('夢幻旅遊景點: ')
    
    # 將輸入存入survey_dict字典
    survey_dict[name] = travel_location

    # 可由此決定是否離開市場調查
    repeat = input('是否有人要參加市場調查(y/n) ')
    if repeat != 'y':
        market_survey = False

# 市場調查結束
print('\n\n以下是市場調查的結果')
for user, location in survey_dict.items():
    print(user, '夢幻旅遊景點: ', location)



