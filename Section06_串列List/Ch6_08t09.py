'''
Python 有內建一些執行統計運算的函數，如果串列內容全部是數值則可以使用max()函數獲取串列的最大值。
min() 函數可以獲得串列的最小值
sum() 函數可以獲得串列的總和
'''

# Ch6_08.py 計算james球員5場的最高分、最低分得分和5場的總得分總計。
james = [23, 19, 22, 31, 18]
highest_score = max(james)
lowest_score = min(james)
total = sum(james)
print(f'Jamse 五場最高分為: {highest_score}, 五場最低分為: {lowest_score}, 總得分為: {total}')

# Ch6_09.py 重新設計Ch6_08.py 但是使用含字串元素的James串列。
James = ['Lebron James', 23, 19, 22, 31, 18]
highest_score = max(James[1:6])
lowest_score = min(James[1:6])
total = sum(James[1:6])
print(f'Jamse 五場最高分為: {highest_score}, 五場最低分為: {lowest_score}, 總得分為: {total}')
