'''
許多時候須將資料視覺化，方便可以直覺看到目前的數據，因此使用matplotlib繪圖庫模組


認識matplotlib.pyplot模組的主要函數

繪製圖表常用函數: 
plot(系列資料)    ---->  繪製折線圖
scatter(系列資料) ---->  繪製散點圖
bar(系列資料)     ---->  繪製長條圖
hist(系列資料)    ---->  繪製直方圖
pie(系列資料)     ---->  繪製圓餅圖


座標軸設定常用的函數:
title(標題)         ----->  設定座標軸的標題
axis()              ----->  可以設定座標軸的最小和最大刻度範圍
xlim(x_Min, x_Max)  ----->  設定x軸的刻度範圍
ylim(y_Min, y_Max)  ----->  設定y軸的刻度範圍
label(名稱)         ----->  設定圖表標籤的圖例
xlabel(名稱)        ----->  設定x軸的名稱
ylabel(名稱)        ----->  設定y軸的名稱
xticks(刻度值)      ----->  設定x軸刻度值
yticks(刻度值)      ----->  設定y軸刻度值
tick_paramse()     ----->  設定座標軸的刻度大小、顏色
legend()           ----->  設定座標的圖例
text()             ----->  在座標軸指定位置輸出字串
grid()             ----->  圖表增加格線
show()             ----->  顯示圖表，每個程式末端皆有此函數
cla()              ----->  清除圖表


圖片的讀取與儲存的函數:
imread(檔案名稱)   ----->  讀取圖片檔案
savefig(檔案名稱)  ----->  將圖片存入檔案
'''

'''
繪製簡單的折線圖plot()

常用的語法格式如下:
plot(x, y, lw=x, ls='x', label='xxx', color)

x: x軸系列值, 如果省略系列自動標記0, 1, ...
y: y軸系列值, 如果省略系列自動標記0, 1, ...
lw: lw 是 linewidth 的縮寫，折線圖的線條寬度
ls: ls 是 linestyle 的縮寫，折線圖的線條樣式
color: 縮寫是 c ，可以設定色彩
label: 圖表的標籤
'''
# Ch20_01.py 繪製折線的應用，square[]串列有9筆資料代表y軸，數據基本上是x軸索引0-8的平方值序列，這個實例使用串列生程式建立x軸數據。
import matplotlib.pyplot as plt

x = [x for x in range(9)]           #產生 0, 1, 2, ...8 串列
squares = [x**2 for x in range(9)]  
plt.plot(x, squares)                #串列squares數據 是y軸的值
plt.show()


'''
在繪製線條時，預設顏色是藍色。
如果x軸的數據是0, 1, ..., n時, 在使用plot()時我們可以省略x軸數據。
'''
# Ch20_02.py 省略x軸數據
squares = [x**2 for x in range(9)]  
plt.plot(squares)                #串列squares數據 是y軸的值
plt.show()

# Ch20_3.py 將軸刻度x軸設為0-8， y軸刻度設為0-70
squares = [x**2 for x in range(9)]  
plt.plot(squares)       #串列squares數據 是y軸的值
plt.axis([0, 8, 0, 70]) #x軸刻度0-8, y軸的刻度0-70
plt.show()

'''
有時候會想要在圖表內增加隔線，這可以讓整個圖表x軸對應的y軸值更加清楚。
可以使用grid()函數。
'''
# Ch20_3_1.py 增加隔線
squares = [x**2 for x in range(9)]  
plt.plot(squares)       #串列squares數據 是y軸的值
plt.axis([0, 8, 0, 70]) #x軸刻度0-8, y軸的刻度0-70
plt.grid()
plt.show()



