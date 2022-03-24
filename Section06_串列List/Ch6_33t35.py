'''
index() 可以傳回特定元素內容第一次出現的索引值，他的使用格式如下:

索引值 = 串列名稱.index(搜索值)

如果搜索值不存在串列會出現錯誤
'''
# Ch6_33.py 傳回搜索索引值得應用
cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
i = cars.index(search_str)
print(f'所搜尋元素{search_str} 第一次出現的位置索引是 {i}')
nums = [7, 12, 30, 12, 40, 9, 8]
search_val = 30
j = nums.index(search_val)
print(f'所搜尋元素{search_val} 第一次出現位置索引是 {j}')

# 如果搜尋值不在串列會出現錯誤，所以在使用前建議可以先使用in運算式(可參考6-10節)，先判斷搜尋值是否在串列內，如果是在串列內，在執行index()方法。
# Ch6_34.py Lebron James一系列比賽得分，由此串列計算他在第幾場得分最高
James = ['Lebron James', 23, 19, 22, 31, 18]
games = len(James)
score_max = max(James[1:games])
i = James.index(score_max)
print(f'{James[0]} 在第{i} 場 得分最高分為{score_max}')

'''
count() 這個方法可以傳回特定元素內容出現的次數，如果搜尋值不在串列會傳回0，它的使用格式如下:

次數 = 串列名稱.count(搜尋值)

'''
# Ch6_35.py
cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
num1 = cars.count(search_str)
print(f'所搜尋元素 {search_str} 出現 {num1} 次')
nums =[7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print(f'所搜尋元素 {search_val} 出現 {num2} 次')

'''
如果搜尋值不再串列會傳回 0
'''

x = [1, 2, 3, 4]
print(x.count(5)) 