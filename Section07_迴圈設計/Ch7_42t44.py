'''
enumerate 物件使用 for 迴圈解析
'''

# Ch7_42.py 繼續設計 Ch6_57.py，將enumerate物件的索引值與元素值解析出來。

drinks = ['coffe', 'milk', 'juice', 'wine']

for drink in enumerate(drinks):
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print('****************')
for drink in enumerate(drinks, 1):
    print(drink)
for count, drink in enumerate(drinks, 1):
    print(count, drink)


# Ch7_43.py 以下是某位NBA球員的前10場得分數據，可參考程式第二行，請用傳統方式列出那些場次得分超過20分以上。 注意場次從第一場開始
scores = [21, 29, 33, 25, 8, 19, 9, 4, 10, 25]
index = 1
for score in scores:
    if score >= 20:
        print(f'場次: {index}, 得分: {score}')
    index += 1

# Ch7_44.py 使用enumerate()重新設計上一題。
scores = [21, 29, 33, 25, 8, 19, 9, 4, 10, 25]
for count, score in enumerate(scores, 1):
    if score >= 20:
        print(f'場次: {count}, 得分: {score}')

