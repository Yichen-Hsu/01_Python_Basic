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