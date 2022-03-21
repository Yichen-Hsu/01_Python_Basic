'''
插入串列元素insert()

insert() 可以再任意位置插入元素
'''

# Ch6_25.py 使用insert() 插入串列元素的應用。
cars = ['Honda', 'Toyota', 'Ford']
print("目前串列內容 = ", cars)
print("在索引1的位置插入Nissan")
cars.insert(1, 'Nissan')
print("目前串列內容 = ", cars)
print("在索引0的位置插入BMW")
cars.insert(0, 'BMW')
print("目前串列內容 = ", cars)

