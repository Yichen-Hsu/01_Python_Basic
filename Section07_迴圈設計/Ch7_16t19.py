# Ch7_16.py 重新設計Ch7_15.py, 進階串列生成的應用。
n = int(input("請輸入整數: "))
if n > 19 : n = 10
squares = [ num ** 2 for num in range (1, n+1)]
print(squares)

# Ch7_17.py 有一個攝氏溫度串列Celcius，這個程式會利用此串列生成華氏溫度串列Fahrenheit。
celcius_list = [21, 25, 29]
fahrenheit_list = [round(n*1.8 + 32,2) for n in celcius_list]
print(fahrenheit_list)

# Ch7_18.py 畢達哥拉斯直角三角形(A Pythagorean triple)定義，其實這是我們國中數學所學的畢氏定理，基本觀念是直角三角形兩邊長的平方和等於斜邊的平方，寫意程式找出1-20內符合a**2 + b**2 = c**2 的組合
pythagorean_group = [[a, b, c] for a in range(1, 21) for b in range(1, 21) for c in range(1, 21) if a**2 + b**2 == c**2]
print(pythagorean_group)

# Ch7_19.py 列出所有元素配對
colors = ['red', 'blue', 'green']
shapes = ['spot', 'line', 'area']
result = [[color, shape] for color in colors for shape in shapes]
print(result)
