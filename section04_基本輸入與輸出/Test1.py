# s = "Python Wrold"
# print(s)
# print(s[0:7:2])

# tuple1 = (3,4,5)
# tuple2 = (3,5,6)
# tuple3 = tuple1 +  tuple2
# print(tuple3)

# list1 = [2,5,7]
# mix = list1 + tuple2
# print(mix)

# print(str(10)+10)

# a = b = 'hello'
# print(id(a))
# print(id(b))

# a = 'hi'
# print(id(a))
# print(b)

# a=11

# print(a%2)

# import numpy as np
# A = np.ones((3,3))
# print(A)

# for k in range(2):
#     print(k,end="")
#     for t in range(2):
#         print(t,end="")

height = float(input("your height:"))
weight = float(input("your weight:"))
print("Your height is: ", height,"\t", "Your weight is: ", weight)
BMI = weight/height**2
print(BMI)
