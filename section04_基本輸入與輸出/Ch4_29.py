
# Ch4_29.py 房屋貸款實作
loan = eval(input("請輸入貸款總金額: "))
year = eval(input("請輸入年限: "))
rate = eval(input("請輸入年利率: "))
monthrate = rate / (12*100) #改成百分比及月利率

# 計算每月還款金額
molecules = loan * monthrate
denominator = 1 - (1 / (1 + monthrate) ** (year * 12 ))
monthlypay = molecules / denominator #每月還款金額
totalpay = monthlypay * year * 12

print(f"每月還款金額{int(monthlypay)}")
print(f"總共還款金額{int(totalpay)}")
