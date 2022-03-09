'''
有些視窗元件在執行時會更改內容，此時可以使用tkinter模組內的變數類別(Variable Class)，它的使用方式如下:

x = IntVar()        #整數變數，預設是0
x = DoubleVar()     #浮點數變數，預設是0.0
x = StringVar()     #字串變數，預設是""
x = BooleanVar()    #布林值變數，True是1，False是0

可以使用get()方法取得變數內容，可以使用set()方法設定變數內容。
'''

# Ch18_14.py 這個程式在執行時，若按hit按鈕可以顯示"I like tkinter"字串，如果已經顯示此字串則改成不顯示此字串
from tkinter import *

def btn_hit():    #處理按鈕事件
    global msg_on #設全域變數
    if msg_on == False:
        msg_on = True
        x.set("I like tkinter") #顯示文字
    else:
        msg_on = False
        x.set("") #不顯示文字

window = Tk()
window.title("Ch18_14")

msg_on = False   #全域變數的預設是FALSE
x = StringVar()  #Label的變數內容

label = Label(window, textvariable=x,        #設定Label內容是變數是x
              fg="blue", bg="lightyellow",   
              font="Verdana 16 bold",
              width=25, height=2).pack()
btn = Button(window, text="Hit", command=btn_hit).pack(side=LEFT)
exitbtn = Button(window, text="exit", command=window.destroy).pack(side=RIGHT)

window.mainloop()