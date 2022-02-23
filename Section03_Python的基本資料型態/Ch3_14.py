'''
3-4 字串資料型態

所謂的字串資料(string)資料是指兩個單引號(')或是兩個雙引號(")之間任意個數字元符號的資料，他的資料型態代號是str。
在英文字串的使用中常會發生某字間有單引號，其實這是文字的一部份。
例: This is Kevin's ball
如果用單引號去處理上述字串將產生錯誤。
所以碰到上述情況則可以用雙引號解決。

x = "This is Kevin's ball"
print(x)
'''

#Ch3_14.py 使用單引號與雙引號設定與輸出資料的應用。

x = "Deepmind means deepen your mind" #雙引號設定字串
print(x)
print(type(x))

y  = '深植智慧 - Deepen your mind'
print(y)
print(type(y))
