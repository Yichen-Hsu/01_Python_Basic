'''
字串的索引

可以使用索引值的方式取得字串內容，索引方式則與串列相同。
'''

# Ch6_45.py 使用正值與負值的索引列出字串元素內容
string = 'python'
# 正值索引
print(f'{string[0] = }')
print(f'{string[1] = }')
print(f'{string[2] = }')
print(f'{string[3] = }')
print(f'{string[4] = }')
print(f'{string[5] = }')
# 負值索引
print(f'{string[-1] = }')
print(f'{string[-2] = }')
print(f'{string[-3] = }')
print(f'{string[-4] = }')
print(f'{string[-5] = }')
print(f'{string[-6] = }')
# 多重指定的概念
s1, s2, s3, s4, s5, s6 = string
print("多重指定觀念的輸出測試 = ", s1, s2, s3, s4, s5, s6)

'''
字串切片
'''

# CH6_46.py 字串切片的應用
string = "Deep Learning" #定義字串
print("列印string第0-2元素  = ", string[0:3])
print("列印string第1-3元素  = ", string[1:4])
print("列印string第1, 3, 5元素  = ", string[1:6:2])
print("列印string第1到最後元素  = ", string[1:])
print("列印string前3元素  = ", string[0:3])
print("列印string後3元素  = ", string[-3:])


# Ch6_47.py 將函數len()、max()、min()應用在字串。
string = "Deeplearning"
strlen = len(string)
print('字串長度', strlen)
maxstr = max(string)
print(f"字串最大的字元{maxstr} 和unicode碼值 {ord(maxstr)}")
minstr = min(string)
print(f"字串最小的字元{minstr} 和unicode碼值 {ord(minstr)}")
