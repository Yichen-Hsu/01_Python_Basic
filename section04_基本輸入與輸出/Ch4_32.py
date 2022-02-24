# Ch4_32.py
'''
雞兔同籠 - 解聯立方程式
籠中有35顆頭、100隻腳，求雞與兔各有幾隻?
'''

heads = int(input("how many heads are there: "))
feet = int(input("how many feet are there: "))
chicken = (4*heads - feet)/2 
rabits = (feet - 2*heads)/2
print(f"there are {int(chicken)} chickens and {int(rabits)} rabits")


