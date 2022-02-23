# divmod() 可以一次取得商和餘數。
# 延續 Ch3_24.py 題目

dist = 384400
speed = 1225
total_hours = dist // speed
days, hours = divmod(total_hours, 24)
print("總共需要天數")
print(days)
print("小時數")
print(hours)