# Ch4_31.py 計算台北車站到澳洲布里斯本的距離
import math
r = 6371 #地球半徑(km)
x1, y1 = -27.3818631, 152.7130055 #布里斯本(緯度，經度)
x2, y2 =  25.0473724, 121.5114737 #台北車站(緯度，經度)

distant = 6371*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                         math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                         math.cos(math.radians(y1-y2)))
print(f"distance = {distant:6.1f} km")