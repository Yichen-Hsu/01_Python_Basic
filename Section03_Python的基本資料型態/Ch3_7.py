'''
我們可以用16進位方式代表整數，python中定義凡是0x開頭的數字，代表這是16進位的整數。
hex()函數 可以將一般數字轉換為16進位
'''

#Ch3_7.py
x = 0x4b7ddda #這是16進位整數
print(x)      #列出十進位整數結果
y = 348291    #這是十進位整數
print(hex(y)) #列出16進位整數結果
