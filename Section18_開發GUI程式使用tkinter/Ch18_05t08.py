'''
設計GUI程式時，可以使用3種方法包裝和定位各元件的位置，這三個方法又稱為 視窗元件配置管理員
'''

'''
pack() 方法
'''
# Ch18_5.py 一個視窗含有3個標籤的應用

from tkinter import *

window = Tk()
window.title("Ch18_5")
lab1 = Label(window, text="Rock n roll",
             bg = "#FFFF00",
             width = 15)
lab2 = Label(window, text="Rock n roll",
             bg = "#ADFF2F",
             width = 15)
lab3 = Label(window, text="Rock n roll",
             bg = "#DB7093",
             width = 15)
lab1.pack()
lab2.pack()
lab3.pack()

window.mainloop()

'''
使用pack()可以讓元件由上往下排列顯示，這也是系統預設。
使用pack()方法時，也可以增加 side參數 設定元件的排列方式

TOP: 這是預設，由上往下排列
BOTTOM: 由下往上排列
LEFT: 有左往右排列
RIGHT: 由右往左排列

如果期待有適度間距，可以增加參數padx/pady，代表水平間距/垂直間距，可以分別在元件增加間距。
'''

# Ch18_6.py 在pack()方法內增加 "side=BOTTOM" 重新設計Ch18_05.py
window = Tk()
window.title("Ch18_5")
lab1 = Label(window, text="Rock n roll",
             bg = "#FFFF00",
             width = 15)
lab2 = Label(window, text="Rock n roll",
             bg = "#ADFF2F",
             width = 15)
lab3 = Label(window, text="Rock n roll",
             bg = "#DB7093",
             width = 15)

lab1.pack(side=BOTTOM)
lab2.pack(side=BOTTOM)
lab3.pack(side=BOTTOM)

window.mainloop()

# Ch18_6_1.py 重新設計Ch18_6.py 在標籤上增加5像素間距。
window = Tk()
window.title("Ch18_5")
lab1 = Label(window, text="Rock n roll",
             bg = "#FFFF00",
             width = 15)
lab2 = Label(window, text="Rock n roll",
             bg = "#ADFF2F",
             width = 15)
lab3 = Label(window, text="Rock n roll",
             bg = "#DB7093",
             width = 15)

lab1.pack(side=BOTTOM)
lab2.pack(side=BOTTOM, pady=5)
lab3.pack(side=BOTTOM)

window.mainloop()

# Ch18_7.py 在pack()方法內增加 "side=BOTTOM" 重新設計Ch18_05.py
window = Tk()
window.title("Ch18_5")
lab1 = Label(window, text="Rock n roll",
             bg = "#FFFF00",
             width = 15)
lab2 = Label(window, text="Rock n roll",
             bg = "#ADFF2F",
             width = 15)
lab3 = Label(window, text="Rock n roll",
             bg = "#DB7093",
             width = 15)

lab1.pack(side=LEFT)
lab2.pack(side=LEFT)
lab3.pack(side=LEFT)

window.mainloop()

# Ch18_7_1.py 重新設計Ch18_7.py 在標籤上增加5像素間距。
window = Tk()
window.title("Ch18_5")
lab1 = Label(window, text="Rock n roll",
             bg = "#FFFF00",
             width = 15)
lab2 = Label(window, text="Rock n roll",
             bg = "#ADFF2F",
             width = 15)
lab3 = Label(window, text="Rock n roll",
             bg = "#DB7093",
             width = 15)

lab1.pack(side=LEFT)
lab2.pack(side=LEFT, padx=10)
lab3.pack(side=LEFT)

window.mainloop()

# Ch18_8.py 在pack()方法內混和使用side參數重新設計ch18_5.py
window = Tk()
window.title("Ch18_5")
lab1 = Label(window, text="Rock n roll",
             bg = "#FFFF00",
             width = 15)
lab2 = Label(window, text="Rock n roll",
             bg = "#ADFF2F",
             width = 15)
lab3 = Label(window, text="Rock n roll",
             bg = "#DB7093",
             width = 15)

lab1.pack()
lab2.pack(side=RIGHT)
lab3.pack(side=LEFT)

window.mainloop()