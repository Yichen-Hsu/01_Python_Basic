'''
grid() 方法

其觀念就如同格狀或是Excel試算表方式，包裝和定位視窗元件的方法，即是使用row(行)和column(列)的參數。
'''

# Ch18_9.py 使用grid()方法取代pack()方法重新設計

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
lab1.grid(row=0, column=0)
lab2.grid(row=1, column=0)
lab3.grid(row=1, column=1)

window.mainloop()


# Ch18_10.py 格狀包裝的另一個應用

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
lab1.grid(row=0, column=0)
lab2.grid(row=1, column=2)
lab3.grid(row=2, column=1)

window.mainloop()

'''
在grid()方法內也可以增加sticky參數，可以用參數設定N/S/W/E, 意義是上/下/左/右對齊。
此外也可以增加padx/pady參數分別設定元件與相鄰元件的x軸間距/y軸間距
'''

# Ch18_10_1.py 使用grid()方法建立8個標籤的應用

from tkinter import *

window = Tk()
window.title("Ch18_10.py")
lab1 = Label(window, text="標籤1", relief="raised").grid(row=0, column=0)
lab2 = Label(window, text="標籤2", relief="raised").grid(row=0, column=1)
lab3 = Label(window, text="標籤3", relief="raised").grid(row=0, column=2)
lab4 = Label(window, text="標籤4", relief="raised").grid(row=0, column=3)
lab5 = Label(window, text="標籤5", relief="raised").grid(row=1, column=0)
lab6 = Label(window, text="標籤6", relief="raised").grid(row=1, column=1)
lab7 = Label(window, text="標籤7", relief="raised").grid(row=1, column=2)
lab8 = Label(window, text="標籤8", relief="raised").grid(row=1, column=3)

window.mainloop()

'''
如果上述標籤2與標籤3的區間是被一個標籤占用時，此時就是使用columnspan參數的場合
若是發生在標籤2與標籤6的區間是被一個標籤占用，此時就是使用rowspan參數的場合
'''

# Ch18_10_2 將標籤2和標籤3合併成一個標籤
from tkinter import *

window = Tk()
window.title("Ch18_10.py")
lab1 = Label(window, text="標籤1", relief="raised").grid(row=0, column=0)
lab2 = Label(window, text="標籤2", relief="raised").grid(row=0, column=1, columnspan=2)
lab4 = Label(window, text="標籤4", relief="raised").grid(row=0, column=3)
lab5 = Label(window, text="標籤5", relief="raised").grid(row=1, column=0)
lab6 = Label(window, text="標籤6", relief="raised").grid(row=1, column=1)
lab7 = Label(window, text="標籤7", relief="raised").grid(row=1, column=2)
lab8 = Label(window, text="標籤8", relief="raised").grid(row=1, column=3)

window.mainloop()

# Ch18_10_3.py 將標籤2和標籤6合併成一個標籤

window = Tk()
window.title("Ch18_10.py")
lab1 = Label(window, text="標籤1", relief="raised").grid(row=0, column=0)
lab2 = Label(window, text="標籤2", relief="raised").grid(row=0, column=1, rowspan=2)
lab3 = Label(window, text="標籤3", relief="raised").grid(row=0, column=2)
lab4 = Label(window, text="標籤4", relief="raised").grid(row=0, column=3)
lab5 = Label(window, text="標籤5", relief="raised").grid(row=1, column=0)
# lab6 = Label(window, text="標籤6", relief="raised").grid(row=1, column=1)
lab7 = Label(window, text="標籤7", relief="raised").grid(row=1, column=2)
lab8 = Label(window, text="標籤8", relief="raised").grid(row=1, column=3)

window.mainloop()
