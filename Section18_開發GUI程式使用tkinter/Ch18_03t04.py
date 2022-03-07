'''
標籤 Label

Label()方法的第一個參數是父物件，表示這個標籤將建立在那一個父物件(可想成父視窗或是一個容器)

下列是Label()方法內其他常用的option參數:

text: 標籤內容，如果有"\n" 則可創造多行文字
width: 標籤寬度，單位是字元。
height: 標籤高度，單位是字元。
bg 或 background: 背景是色彩
fg 或 froeground: 字形色彩
font(): 可選擇字形與大小
textvariable: 可以設定標籤以變數方式顯示
image: 標籤以圖形方式呈現
relief: 預設是relief=flat，可由此控制標籤的外框
justify: 在多行文件時最後一行的對齊方式 left/center/right, 預設是置中對齊
'''

# Ch18_3.py 建立一個標籤，內容是 I like tkinter

from tkinter import *

window = Tk()
window.title("Ch18_3")  #建立視窗標題
label = Label(window, text="I like tkinter")
label.pack()            #包裝與定位元件

window.mainloop()

# Ch18_3_1.py 使用Label().pack()方式重新設計 Ch18_3.py

window = Tk()
window.title("Ch18_3_1")
label = Label(window, text="I love tkinter").pack()

window.mainloop()

# Ch18_4.py 擴充Ch18_3.py 標籤寬度是15, 背景顏色為淺黃色
window = Tk()
window.title("Ch18_4")
label = Label(window, text="I like tkinter", 
              bg = "lightyellow",               #標籤背景為淺黃色
              width = 15                        #標籤寬度是15
              )
label.pack()     #包裝與定位元件

window.mainloop()

# Ch18_4_1.py 重新設計Ch18_4.py，使用font更改字形與大小的應用。
window = Tk()
window.title("Ch18_4_1")
label = Label(window, text="I like tkinter", 
              bg = "lightyellow",               #標籤背景為淺黃色
              width = 15,                        #標籤寬度是15
              font = "Helvatica 16 bold italic"  # Helvatica是字體 16是字形大小 bold是粗體 italic是斜體, 如果不設定則是預設一般字體
              )
label.pack()

window.mainloop()