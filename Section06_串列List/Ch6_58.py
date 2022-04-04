'''
製作大型的串列資料

有時我們想要製作更大型的串列資料結構，例如：串列的元素是串列，可以參考以下實例。
'''
asia = ['Taiwan', "Japan", 'Korea']
the_usa = ['Chicago', 'New York', 'Los Angeles']
europe = ['France', 'Itali', 'Roman']

area = [asia, the_usa, europe]
print(area)

'''
使用者帳號管理系統
'''
# Ch6_58.py 設計一個帳號管理系統，這個程式分成2個部分，第一個部分是建立帳號，讀者的輸入將會存在accounts串列。第二部分是要求輸入帳號，如果輸入正確會輸出"歡迎進入系統"，如果輸入錯誤會輸出"帳號錯誤"

accounts = []
account = input("請輸入新帳號: ")
accounts.append(account)

print("---公司系統---")

ac = input("請輸入帳號: ")
if ac in accounts:
    print("歡迎進入公司系統")
else:
    print("帳號密碼錯誤")


'''
凱薩密碼

凱薩密碼的加密觀念是將每個英文字母往後移，對應至不同字母，只要記住所對應的字母，就可以解密。
'''

abc = 'abcdefghijklmnopqrstuvwxyz'
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
print(subText)