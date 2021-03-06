# Python 裡面的help() 可以列出某一個指令或函數的使用說明。
# 例如: Help(print) 及是 詢問print 於 python裡所代表的意義。
help(print)

'4-2-1 函數Print()的基本寫法'
'它的基本語法格式如下:'
'print(value, ... , sep="", end="\n", file=sys.stdout, flush=false)'

# Value 表示想要輸出的資料，可以一次輸出多筆資料，個資料可以以逗號隔開。
# Sep 當輸出多筆資料時，可以插入各筆資料的分隔字元，預設是一個空白字元。
# End 當資料輸出結束時所插入的字元，預設是插入換行字元，所以下一次print()函數的輸出會在下一行輸出。
#     如果想下一次輸出不換行，可以在此設定空字串，或是空格或是其他字串。
# File 資料輸出位置，預設是sys.stdout，也就是螢幕。也可以使用此設定，將輸出導入其他檔案、或設備。
# Flush 是否清除資料流的緩衝區，預設是不清除。

"Ch4_1.py: 重新設計 Ch3_18.py，其中在第二個print()，2筆輸出資料的分隔字元是$$$。"
num1 = 222
num2 = 333
num3 = num1 + num2
print("這是數值相加", num3)
str1 = str(num1) + str(num2)
print("強制轉換為字串相加", str1, sep=" $$$ ")


