'''
input() 讀取使用者鍵盤輸入的資料，輸入input後輸出的結果皆是字串
'''

# Ch4_22.py 輸入資料類型
name = input("your name: ")
score = input("your score: ")
print(f"your name is {name}")
print(f"your score is {score}")

# Ch4_23.py 基本資料輸入與運算
print("Welcome to use Name and Score insert system")
name = input("input you name: ")
score1 = input("your score1: ")
score2 = input("your score2: ")
total = int(score1) + int(score2)
print(f"Hello {name}, your total score is {total}")

# Ch4_24.py 改成字串相加輸出
name = input("your first name is: ")
l_name = input("your last name is: ")
full_name = name + l_name
print(f"hello {full_name} welcome to python world")


