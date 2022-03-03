print(dir(__builtins__)) #可以列出所有python的內建函數

# Ch4_28.py 請輸入華氏溫度並輸出攝氏溫度

fahrentheit = float(input("The degrees of fahrentheit: "))
celsius = (fahrentheit - 32) * 5 / 9
print(f'華氏{fahrentheit}度 = 攝氏{celsius:.2f}度')

