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

