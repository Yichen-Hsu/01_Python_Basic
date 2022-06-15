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

