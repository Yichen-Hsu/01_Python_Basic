'''
刪除串列元素


可以使用下列方式刪除指定索引的串列元素: 

del mylist[i]  刪除索引i的串列元素

下列是刪除串列區間元素

del mylist[start:end] 刪除索引從start到end-1索引的串列元素

下列是刪除區間，但是用step作為每隔多少區間再刪除。

del mylist[start:end:step] 每隔step, 刪除從索引start到end-1索引的串列元素
'''

# Ch6_17.py 如果NBA勇士隊主將陣容有5名，其中一名隊員bell離隊了，可用下列方式設計。
warriors = ['Curry', 'Durant', 'Iquodala', 'Bell', 'Thompson']
print('2018年初NBA勇士隊的主將陣容', warriors)
del warriors[3]
print('2018年初NBA勇士隊的主將陣容', warriors)

# Ch6_18.py 刪除串列元素的應用
nums1 = [1, 3, 5]
print("刪除nums1串列索引1元素前 = ", nums1) 
del nums1[1]
print("刪除nums1串列索引1元素後 = ", nums1)
nums2 = [1, 2, 3, 4, 5, 6]
print("刪除nums2串列索引[0:2]元素前 = ", nums2)
del nums2[0:2]
print("刪除nums2串列索引[0:2]元素後 = ", nums2)
nums3 = [1, 2, 3, 4, 5, 6]
print("刪除nums3串列索引[0:6:2]元素前 = ", nums3)
del nums3[0:6:2]
print("刪除nums3串列索引[0:6:2]元素後 = ", nums3)