'''
eval() 函數可以直接傳回字串表達式的計算結果
'''

# Ch4_25.py 輸入公式，可以列出計算結果。
nubmerstring = input("plese input how you want to calculate your numbers: ")
number = eval(nubmerstring)
print(f"the result is {number:5.2f}")

# Ch4_26.py 使用eval()重新設計
print("Welcome to use Name and Score insert system")
name = input("input you name: ")
score1 = input("your score1: ")
score2 = input("your score2: ")
total = eval(score1) + eval(score2)
print(f"Hello {name}, your total score is {total}")

# Ch4_27.py 

n1, n2 ,n3 = eval(input("your numbers: "))
average = (n1 + n2 + n3)/3
print(f"the average is {average:.2f}")