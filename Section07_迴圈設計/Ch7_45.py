# Ch7_45.py 設計購物車系統
store = 'Hi there store'
products = ['Television', 'Washing Machine', 'Fans', 'Air Conditioner']
cart = []
print(store)
print(products, '\n')
while True:
    msg1 = ('if you want to leave this program please type q to quit')
    msg = input('please enter the item you need: ')
    if msg == 'q':
        break
    else:
        if msg in products:
            cart.append(msg)
print('The items in cart are: ', cart)
    