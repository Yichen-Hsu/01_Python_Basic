name = '許詣承'
len(name)
print(len(name))
nameBytes = name.encode('utf-8')
len(nameBytes)
print(len(name))
type(nameBytes)
print(type(nameBytes))
print(nameBytes)

# 3-7-1 計算地球到月球所需時間

'從地球到月球約是384400公里，假設火箭的速度是一馬赫，設計一個程式計算需多少天、多少小時才可抵達月球。這個程式省略分鐘數。'

dist =  384400
speed = 1225
total_hours = dist // speed
days = total_hours // 24
hours = total_hours % 24
print("總共需要天數")
print(days)
print("小時數")
print(hours)