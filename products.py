products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    # products.append(name)
    price = input('請輸入商品價格：')
    # p = [name, price]
    # p.append(name)
    # p.append(price)
    # products.append(p)
    # 下面寫法為上面 8 ~ 11 的簡寫法
    products.append([name, price])
    
print(products, "\n")
# print(products[0][0])

for p in products:
    print(p[0], '的價格是', p[1])
    #