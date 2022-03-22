'''
顛倒排序 reverse()

reverse() 可以顛倒排序串列的元素，顛倒後即是永久修改，欲改回則再下一次指令即可。

另一方面，也可以使用[::-1]方式取得串列顛倒排序，但原串列順序並未改變。
'''
# Ch6_28.py 使用2種方式執行顛倒排序串列元素
from audioop import reverse


nums = [1, 2, 3, 4, 5, 6, 7]
print('目前串列內容 = ', nums)
# 直接使用[::-1]顛倒排序不更改內容
print("使用[::-1]方式顛倒排序，不更改串列內容 = ", nums[::-1])
# 更改串列內容
print("使用reverse()顛倒排序串列元素")
nums.reverse()
print("新的串列內容為: ", nums)


'''
sort() 排序

sort()方法可以對串列元素由小到大排序，這個方法可以同時對純數值元素與船英文字串元素字串有非常好的效果。
經排序後原串列的元素順序會被永久更改。

如果是排序英文字串，建議先將字串英文字元全部改成大寫或全部改成小寫。
'''

# Ch6_29.py 數字與英文字串元素排序的應用
english_nums = ['one', 'two', 'four', 'six', 'eleven']
print('目前串列內容 = ', english_nums)
print("使用sort()由小排到大")
english_nums.sort()
print('排序的結果為: ', english_nums)
nums = [93, 29 ,105, 39, 95]
print('目前串列內容 = ', nums)
print("使用sort()由小排到大")
nums.sort()
print('排序的結果為: ', nums)

# 上述內容是由小排到大，sort()方法是允許由大排到小，只要在sort()內增加參數 "reverse=True" 即可。

# Ch6_30.py 將字串列元素由大排到小
english_nums = ['one', 'two', 'four', 'six', 'eleven']
print('目前串列內容 = ', english_nums)
print("使用sort()由小排到大")
english_nums.sort(reverse=True)
print('排序的結果為: ', english_nums)
nums = [93, 29 ,105, 39, 95]
print('目前串列內容 = ', nums)
print("使用sort()由小排到大")
nums.sort(reverse=True)
print('排序的結果為: ', nums)

'''
sorted() 排序

若不希望更改串列元素順序，可以使用另外一種排序sorted()。
使用這種排序可以獲得想要的排序結果，我們可以用新串列儲存新的排序串列，同時原先串列的順序將不更改。
使用格式如下: 
newlist = sorted(mylist)
'''

# Ch6_31.py sorted()排序的應用。
hi = ['aloha', 'como esta', 'ni hao', 'its a nice day for fishing aint it']
print('目前串列內容 = ', hi)
print('使用sorted()由小排到大')
hi_sorted = sorted(hi)
print('排序串列結果 = ', hi_sorted)
print('原先串列hi內容 = ', hi)

nums = [2, 6 ,3 ,10, 7, 9]
print('目前串列內容 = ', nums)
print('使用sorted()由小排到大')
nums_sorted = sorted(nums)
print('排序串列結果 = ', nums_sorted)
print('原先串列hi內容 = ', nums)

# 如果我們想要從大排到小，可以在sorted()內增加參數 "reverse=True"
hi = ['aloha', 'como esta', 'ni hao', 'its a nice day for fishing aint it']
print('目前串列內容 = ', hi)
print('使用sorted()由大排到小')
hi_sorted = sorted(hi, reverse=True)
print('排序串列結果 = ', hi_sorted)
print('原先串列hi內容 = ', hi)

nums = [2, 6 ,3 ,10, 7, 9]
print('目前串列內容 = ', nums)
print('使用sorted()由大排到小')
nums_sorted = sorted(nums, reverse=True)
print('排序串列結果 = ', nums_sorted)
print('原先串列hi內容 = ', nums)
