'''
3-4-8 字串前加r

在使用Python時，如果在字串前加r，可以防止逸出字元(Escape Character)被轉譯，可參考3-4-3的溢出字元表，相當於可以取消逸出字元的功能
'''
### 何謂逸出字元 ###
'''複習: 就是前面需要有"\"(反斜線)的特殊字元'''

#Ch3_22.py: 字串前加r的應用
str1 = "Hello!\nPython!"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython!"
print("含r字元的輸出")
print(str2)

