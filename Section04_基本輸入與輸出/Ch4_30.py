# Ch4_30.py 正五角形面積
import math

s = eval(input("請輸入正五角形邊長: "))
area = (5 * s ** 2) / (4 * math.tan(math.pi/5))
print(f"{area = :6.2f}")