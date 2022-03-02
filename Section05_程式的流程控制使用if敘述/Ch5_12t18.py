# Ch5_12.py BMI Evaluation
height = eval(input("please enter your height in cm: "))
weight = eval(input("please enter your weight in kg: "))
bmi = weight / (height/100) ** 2
if bmi >= 18.5 and bmi < 24:
    print(f"{bmi = :5.2f} typeical weight")
else:
    print(f"{bmi = :5.2f} abnormal weight")

# Ch5_13.py guess numbers 0 ~ 7
ans = 0
print("please keep a number in your mind from 0 to 7, and answer the question")
truefalse = "etner y/Y to commit the showing number is in your mind. Otherwise, nope."
# 檢測二進位的第1位是否含1
q1 = "有沒有看到心中的數字: \n" + \
     "1, 3, 5, 7 \n"
num = input(q1 + truefalse)
print(num)
if num == "y" or num == "Y":
    ans += 1
# 檢測二進位的第2位是否含1
q1 = "有沒有看到心中的數字: \n" + \
     "2, 3, 6, 7 \n"
num = input(q1 + truefalse)
print(num)
if num == "y" or num == "Y":
    ans += 2
# 檢測二進位的第3位是否含1
q1 = "有沒有看到心中的數字: \n" + \
     "4, 5, 6, 7 \n"
num = input(q1 + truefalse)
print(num)
if num == "y" or num == "Y":
    ans += 4

print(f"the number in your mind is: {ans}")

# Ch5_14.py 12生肖系統
year = eval(input("請輸入你的西元出生年: "))
year -= 1900
zodiac = year % 12
if zodiac == 0:
    print("你的生肖是: 鼠")
elif zodiac == 1:
    print("你的生肖是: 牛")
elif zodiac == 2:
    print("你的生肖是: 虎")
elif zodiac == 3:
    print("你的生肖是: 兔")
elif zodiac == 4:
    print("你的生肖是: 龍")
elif zodiac == 5:
    print("你的生肖是: 蛇")
elif zodiac == 6:
    print("你的生肖是: 馬")
elif zodiac == 7:
    print("你的生肖是: 羊")
elif zodiac == 8:
    print("你的生肖是: 猴")
elif zodiac == 9:
    print("你的生肖是: 雞")
elif zodiac == 10:
    print("你的生肖是: 狗")
else:
    print("你的生肖是: 豬")

# Ch5_15.py 求一元二次方程式的根 ax**2 + bx + c = 0
'''root1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a), root2 = (-b - (b**2 - 4*a*c)**0.5/(2*a)'''
a = int(input("please enter the contant of sequre of x: "))
b = int(input("please enter the contant number of x: "))
c = int(input("please enter the final number of constant in the end of function: "))

r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(f"the answers are {r1:.2f} and {r2:.2f}")

# Ch5_16.py 求解聯立方程式
'''
設 ax + by = c, dx + ey = f
則 x = (ce - bf)/(ae - db), y = (cd - af)/(bd - ae)
'''
a = int(input("the constant in front of x in the first function: "))
b = int(input("the constant in front of y in the first function: "))
c = int(input("the final constant in the rest of function: "))
d = int(input("the constant in front of x in the second function: "))
e = int(input("the constant in front of x in the second function: "))
f = int(input("the final constant in the rest of function: "))

x = (c*e - b*f)/(a*e - d*b)
y = (c*d - a*f)/(b*d - a*e)

print(f"the answer x = {x:.2f}, y = {y:.2f}")

# Ch5_17.py 火箭升空
'''
第一宇宙速度(環繞地球速度), 速度是 7.9 km/s, 當火箭達到此速度將繞著地球作圓形運動，但若是介於7.9km/s與11.2km/s則做橢圓形運動。
第二宇宙速度(脫離速度), 若速度到達11.2km/s與16.7km/s之間，則可以環繞太陽。
第三宇宙速度(脫逃速度)， 超過16.7km/s則可以脫離太陽引力至外太空。
'''
v = eval(input("請輸入火箭速度: "))
if v < 7.9:
    print("無法進入太空")
elif v== 7.9:
    print("第一宇宙速度")
elif v > 7.9 and v < 11.2:
    print("繞地球做橢圓形運動")
elif v > 11.2 and v < 16.7:
    print("人造衛星環繞太陽系")
else:
    print("和太陽系說掰掰")


# Ch5_18.py 閏年計算程式
print("判斷是否為閏年")
year = int(input("請輸入西元年份: "))
rem4 = year % 4
rem100 = year % 100
rem400 = year % 400
if rem4 == 0:
    if rem100 != 0 or rem400 == 0:
        print(f"{year}是閏年")
    else:
        print(f"{year}不是閏年")
else:
    print(f"{year}不是閏年")