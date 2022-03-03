# '''
# 使用等差數列求1加至100解為何? 
# '''

x = int(input("the first number: "))
y = int(input("the last number: "))
total = (x + y) * (y - x + 1)/2
print(f"the sum from first number to the last number is {int(total)}")

# another solution
# i = int(input("start number: "))
# scale = int(input("the end number: "))
# loops = scale - i + 1
# total = list()
# for _ in range(loops):
#     total.append(i)
#     i += 1
# print(total)
# print(sum(total[:]))