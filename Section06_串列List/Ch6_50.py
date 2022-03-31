'''
子字串搜尋與索引

相關參數如下:

find(): 從頭找尋子字串如果找到回傳第一次出現索引，如果沒找到回傳-1。
rfind(): 從尾找尋子字串如果找到回傳最後結果出現索引，如果沒找到回傳-1。
index(): 從頭找尋子字串如果找到回傳第一次出現索引，如果沒找到產生例外錯誤。
rindex(): 從尾找尋子字串如果找到回傳最後結果出現索引，如果沒找到產生例外錯誤。
count(): 列出子字串出現次數。
isalnum(): 判斷字串是否只有字母或是數字。

'''

mystr = "Hello World Test test 1 2 3 Test test 1 2 3"
s = 'Test'
k = 'Hello'
error = 'ok'
print(mystr.find(s))
print(mystr.index(s))
print(mystr.rfind(k))
print(mystr.rindex(k))
print(mystr.count(s))
print(mystr.find(error))
# print(mystr.index(error))

'''
字串的其他方法

startswith() 可以列出字串啟始文字是否是特定子字串，如果為真回傳True，否則回傳False
endswith() 可以列出字串結束文字是否是特定子字串，如果為真回傳True，否則回傳False
replace(ch1, ch2): 將ch1字串由另一字串取代。
'''

# Ch6_50.py 列出字串"CIA"是不是啟始或結束字串，以及出現次數。最後這個程式會將Linda字串用Lxx字串取代。
msg = '''CIA Mark told CIA Linda that the secret USB had given to CIA Peter'''
print('字串開頭是CIA: ', msg.startswith("CIA"))
print('字串結束是CIA: ', msg.endswith("CIA"))
print('CIA出現的次數: ', msg.count("CIA"))
msg = msg.replace('Linda', 'Lxx')
print("新的內容為: ", msg)
