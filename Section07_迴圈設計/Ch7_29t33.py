'''
while 迴圈

這也是一個基本的迴圈，基本上迴圈會一直執行直到條件運算為False才會離開迴圈
所以設計while迴圈時一定要設計一個條件可以離開迴圈
程式設計時，如果忘記設計條件可以離開迴圈 可以同時按下ctrl+c中斷程式的執行
'''

# Ch7_29t31.py 這個程式會輸出你所輸入的內容，當輸入q時，程式才會執行結束。
msg = '此程式將複述輸入內容'
msg2 = '按下q即可離開程式'
print(msg, msg2)
while True:
    msg3 = input("請輸入任意內容: ")
    if msg3 != 'q':
        print(msg3)
    else:
         break

# Ch7_32.py 猜數字遊戲，程式第二行用變數 answer 儲存欲猜的數字，程式執行時用guess儲存所猜的數字
answer = 30
guess = 0 
while guess != answer:
    guess = int(input("請猜1-100間的數字: "))
    if guess > answer:
        print("請猜小一點")
    elif guess < answer:
        print("請猜大一點")
    else:
        print("恭喜答對了")

'''
認識哨兵值(Sentinel Value)

在程式設計時，我們可以在while迴圈中設定一個輸入數值當作迴圈執行結束的值，這個值稱為哨兵值(Sentinel Value)
'''

# Ch7_33.py 計算輸入值的總和，哨兵值是0，如果輸入0則是結束程式
n = int(input("請輸入一個值: "))
sum = 0
while n:
    sum += n
    n = int(input("請輸入一個值: "))
print("輸入總和 = ", sum)