'''
place()方法

這是使用place方法內的 x和y參數 直接設定視窗元件的左上方位置，單位是像素，視窗顯示區的左上角是(x=0, y=0), x是往右遞增, y是往下遞增
同時使用這方法時，視窗將不會自動調整大小而是使用預設大小顯示
'''

# Ch18_11.py 使用 place() 方法直接設定標籤的位置

from tkinter import *

window = Tk()
window.title("Ch18_09")
lab1 = Label(window, text="Rock n roll",
             bg = "#FFFF00",
             width = 15)
lab2 = Label(window, text="Rock n roll",
             bg = "#ADFF2F",
             width = 15)
lab3 = Label(window, text="Rock n roll",
             bg = "#DB7093",
             width = 15)
lab1.place(x=0, y=0)
lab2.place(x=30, y=50)
lab3.place(x=60, y=100)

window.mainloop()


'''
************************
使用tkinter模組設計GUI程式時，雖可以使用place()方法定位元件的位置，不過仍建議盡量使用pack()和grid()方法定位元件的位置，
因為當視窗元件一多時，使用place()需計算元件位置較不方便，同時若有新增或減少元件時又須重新開始計算設定元件位置，這樣會較不方便。
************************
'''