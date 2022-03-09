'''
Button 功能鍵

在視窗元件中設計一功能按鈕執行某一個特定的動作

使用格式如下:

Button(父物件, options, ...)

第一個參數是父物件，表示這個功能按鈕建立在那一個視窗內。
下列是Button()方法內其他常用的options參數:

text: 功能扭名稱
width: 寬，單位是字元寬
height:高，單位是字元高
bg或background: 背景色彩
fg或froeground: 字形色彩
image: 功能扭上的圖形
command: 按一下功能鈕時，執行此所指定的方法
'''

# Ch18_12.py 按一下功能鈕時，可以顯示字串 I love Python, 底色是淺黃色，字串顏色是藍色。

from tkinter import *
from turtle import left, right

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"

window = Tk()
window.title("Ch18_12")
label = Label(window)
btn = Button(window, text="Message", command=msgShow)

label.pack()
btn.pack()

window.mainloop()

# Ch18_13.py 擴充設計 Ch18_12.py, 若按Exit鈕，視窗可以結束。

window = Tk()
window.title("Ch18_12")
label = Label(window)
btn = Button(window, text="Message", command=msgShow)
exit = Button(window, text="Exit", command=window.destroy)

label.pack()
btn.pack(side=LEFT)
exit.pack(side=RIGHT)

window.mainloop()

'''
window.destroy 可以關閉 window視窗物件，同時程式結束。
另一個常用的是window.quit 可以讓Python shell內執行的程式結束，但是window視窗則繼續執行
'''

'''
設定視窗背景config()

config(option=value) 是視窗元件的共通方法，透過設定option為bg參數時，可以設定視窗元件的背景顏色
'''

def yellow():
    window.config(bg="yellow")
def blue():
    window.config(bg="blue")

window = Tk()
window.title("ch18_13_1")
window.geometry("300x200") #固定視窗大小
# 依次建立三個按鈕
exitbtn = Button(window, text="Exit", command=window.destroy)
bluebtn = Button(window, text="Blue Background", command=blue)
yellowbtn = Button(window, text="Yellow Background", command=yellow)
# 將三個按鈕包裝定位在右下方
exitbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5) #anchor參數用來指定元件在父容器中的9個錨定方位 E/W/N/W/NW/SW/NE/SE/ CENTER為(預設值)
bluebtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
yellowbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)

window.mainloop()

'''
使用lambda表達式的好時機

yellow按鈕和blue按鈕是執行相同工作，但是所傳遞的顏色參數不同，其實這是用lambda表達式的好時機，我們可以透過lambda表達式呼叫相同的方法，但是傳遞不同參數化方式簡化設計。
'''

# Ch18_13_2.py 使用lambda表達式重新設計

def bColour(bgColour):
    window.config(bg=bgColour)

window = Tk()
window.title("ch18_13_2")
window.geometry("300x200") #固定視窗大小
# 依次建立三個按鈕
exitbtn = Button(window, text="Exit", command=window.destroy)
bluebtn = Button(window, text="Blue Background", command=lambda:bColour("blue"))
yellowbtn = Button(window, text="Yellow Background", command=lambda:bColour("yellow"))
# 將三個按鈕包裝定位在右下方
exitbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5) #anchor參數用來指定元件在父容器中的9個錨定方位 E/W/N/W/NW/SW/NE/SE/ CENTER為(預設值)
bluebtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
yellowbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)

window.mainloop()

'''
上述也可以省略地4-5行的bColour()函數，此時將lambda將改成下列:
command=lambda:window.config(bg="blue")
command=lambda:window.config(bg="yellow")
'''
