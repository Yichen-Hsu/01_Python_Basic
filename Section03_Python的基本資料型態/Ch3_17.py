
#在字串使用中，如過字串內有一些特殊字元，例如:單引號、雙引號...等，必須在此特殊字元前加"\"，才可以正常使用
#這種含有'\'符號的字元稱 逸出字元 (Escape Character)

#逸出字元    Hex值   意義
#\'          27      單引號
#\"          22      雙引號
#\\          5C      反斜線
#\a          07      響鈴
#\b          08      BackSpace鍵
#\f          0C      換頁
#\n          0A      換行
#\o                  8進位表示
#\r          0D      游標移直最左位置
#\x                  16進位表示
#\t          09      Tab鍵效果
#\v          0B      垂直定位

#字串使用中特別是碰到字串含有單引號時，如果你是使用單引號定義這個字串時
#必須要使用此逸出字元，才可以順利顯示
#如果是使用雙引號定義字串則可不必使用逸出字元

#Ch3_17.py 逸出字元的應用

#以下輸出使用單引號設定的字串，需使用\'
str1 = 'I can\'t stop loving you.'
print(str1)
#以下輸出使用雙引號設定的字串，不須使用\'
str2 = "I can't stop loving you."
print(str2)
#以下輸有\t和\n字元
str3 = "I \tcan't stop \nloving you."
print(str3)

