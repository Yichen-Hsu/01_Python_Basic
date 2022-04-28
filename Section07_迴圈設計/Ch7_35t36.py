'''
巢狀while迴圈
'''

# Ch7_35.py 使用while迴圈重新設計Ch7_21.py 列印9*9乘法表
i1 = 1
while i1 < 10:
    i2 = 1
    while i2 < 10:
        times = i1 * i2
        print(f'{i1}*{i2} = {times}', end=" ")
        i2 += 1
    print()
    i1 += 1

'''
強制離開while迴圈，break指令

如果期待抹些條件時發生時可以離開迴圈，可以在迴圈內執行break指令
'''
# Ch3_36.py 這個程式會先建立while無限迴圈，如果輸入q，則可跳出這個while無限迴圈，程式內容主要是要求輸入水果，然後輸出此水果

while True:
    x = input('請輸入一種水果: ')
    if x == 'q':
        print('程式終止')
        break
    else:
        print(f'找{x}有什麼事?')
