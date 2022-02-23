'''
開啟一個檔案 open()

open() 函數可以開啟一個檔案供讀取或寫入，如果這個函數執行成功，會回傳檔案匯流物件，這個函數基本使用如下:
    
    file_Obj = open(file, mode="r")

    其中
    file 為欲開啟的檔案，如果不指名路徑則開啟當前目錄資料夾。
    mode 為開啟檔案的模式，mode可以省略，僅寫欲開啟的模式代號
         代號分別為:
         r: 此為預設，開啟檔案供讀取(read)
         w: 開啟檔案供寫入，如果原先檔案有內容將會被覆蓋(write)
         a: 開啟檔案供寫入，如果原先檔案有內容將會被新增在後面(append)
         x: 開啟一個新的檔案供寫入，如果所開啟的檔案已經存在則會產生錯誤
'''

# Ch4-21.py 將資料輸出到檔案的實例，其中輸出到out1.txt採用"w"模式，輸出到out2.txt採用"a"模式

s1 = open("D:\\01. Work Files\\08. Projects\\02_Python\\第四章 基本輸入與輸出\\output_txt\\out1.txt", "w")
print("Testing for output", file=s1)
s1.close()
s2 = open("D:\\01. Work Files\\08. Projects\\02_Python\\第四章 基本輸入與輸出\\output_txt\\out2.txt", "a")
print("Testing for output", file=s2)
s2.close()
