'''
認識元組

元組具有安全、內容不會被竄改、資料結構單純、執行速度快等優點，
所以其實被大量應用在系統程式設技師，程式設計師喜歡將程式設計所保留的資料以元組儲存。

divmod() 函數的回傳值是商和餘數(元組型態)

商, 餘數 = divmod(被除數, 除數)
'''

# Ch8_19.py 計算地球到月球的時間
dist = 384400
speed = 1225
total_hours = dist // speed
data = divmod(total_hours, 24)
print('divmod傳回的資料型態是: ', type(data))
print(f'總共需要{data[0]}天')
print(f'{data[1]} 小時')