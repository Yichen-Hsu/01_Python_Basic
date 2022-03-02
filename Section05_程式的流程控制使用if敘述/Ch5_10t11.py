# Ch5_10.py 計算BMI指數
height = eval(input("please enter your height: "))
weight = eval(input("please enter your weight: "))
bmi = weight / (height/100) ** 2
if bmi >= 28:
    print(f"your bmi is {bmi:.2f}, over weight")
else:
    print(f"your bmi is {bmi:.2f}, not over weight")

# Ch5_11.py 用新的if用法重新設計上述程式，將上述第四和第五行合併。
height = eval(input("please enter your height: "))
weight = eval(input("please enter your weight: "))
if bmi := weight / (height/100) ** 2 >= 28:
    print(f"your bmi is {bmi:.2f}, over weight")
else:
    print("not over weight")
