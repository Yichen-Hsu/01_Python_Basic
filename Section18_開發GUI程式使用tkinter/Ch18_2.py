from tkinter import *

window = Tk()
window.title("MyWindow")
window.geometry("300x600")
window.resizable(0,0)
window.mainloop()

'''
.title("視窗標題")
.geometry("300x400") 視窗的寬與高，單位是像素
.maxsize(width, height) 拖曳時可以設定視窗最大的寬與高
.resizeable(True, True) 可設定是否更改視窗大小，第一個是寬，第二個是高。 若要固定視窗寬與高則使用 resizeable(0,0)
'''