'''
3-4-2 處理多於一行的字串

程式設計時如果字串長度多於一行，可以使用三個單引號(或是三個雙引號)將字串包夾即可。
另外需留意，如果字串多於一行我們往往會使用按Enter鍵方式來處理，造成字串間多了分行符號。
如果避免這種現象，可以在行末端加上"\"符號，這樣可以避免字串內增加分行符號

另外，也可以使用"符號，但是在定義時再行末增加"\"，或是使用小括號定義字串
'''

#Ch3_16.py 使用三個單引號處理於一行的字串，str1的字串內增加了分行符號，str2字串是連續的沒有分行符號。
str1 = '''Silicon Stone Education is an unbiased organization
concentrated on bridging the gap...'''
print(str1) #字串內有分行符號
str2 = '''Silicon Stone Education is an unbiased organization \
    concentrated on bridging the gap...'''
print(str2) #字串內沒有分行符號
str3 = "Silicon Stone Education is an unbiased organization " \
    "concentrated on bridging the gap..."
print(str3) #使用\符號
str4 = ("Silicon Stone Education is an unbiased organization "
        "concentrated on bridging the gap...")
print(str4) #使用小括號