# Ch5_7.py
print("計算最終成績")
score = int(input("please enter you score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 50:
    print("E")
else:
    print("F")

# Ch5_8.py
print("判斷輸入字元類別")
ch = input("please enter a letter: ")
if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
    print("It's a capital letter. ")
elif ord(ch) >= ord("a") and ord(ch) <= ord("z"):
    print("It's a lowercase letter. ")
elif ord(ch) >= ord("0") and ord(ch) <= ord("9"):
    print("It's a number.")
else:
    print("It's a special letter. ")