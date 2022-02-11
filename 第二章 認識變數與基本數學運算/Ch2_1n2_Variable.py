#變數是一個暫時儲存資料的地方，使用 "=" 設定變數的內容。
#變數就是數學式常用的 x, y, z, ...etc之類的
#開啟Python儲存運算的檔案，此檔案就稱為"程式"
#下述及為變數使用例子
x = hourly_salary = 125                         #設定時薪   
y = annual_salary = hourly_salary * 8 * 300     #計算年薪
z = monthly_fee = 9000                          #設定每月花費
a = annual_fee = monthly_fee * 12               #計算每年花費
b = annual_savings = annual_salary - annual_fee #計算每年儲存金額
print(annual_savings)                           #列出每年儲存金額
'''
變數的命名原則
必須由"英文字母、_(底線)或中文字母開頭，建議使用英文字母
變數名稱只能由英文字母、數字、_(底線)或中文字組成，底線開頭的變數會特別處理
英文字母的大小寫是敏感的，例如 A 與 a 被視為不同變數名稱
Python 系統保留字(或稱關鍵字)不可當作變數名稱，會讓程式發生錯誤
Python 內建函數名稱不建議當作變數名稱因為會造成函數失效。

註:雖然變數名稱可以使用中文字但是不建議，因為是怕將來會有相容性問題。

若要查詢Python內部內建保留字(關鍵字)可以打

help('keywords')查詢

'''
