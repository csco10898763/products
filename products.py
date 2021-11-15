products = []
# 讀取檔案
with open('products.csv', 'r') as f:
    for line in f:
        if '商品,價格' in line:
            continue # 跳到下一次迴圈的意思
        name, price = line.strip().split(',') # strip() 去掉跳行符號 \n & 資料以 ',' 作為分割
        products.append([name, price])
print(products)

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    # products.append(name)
    price = int(input('請輸入商品價格：'))
    # price = int(price)
    # p = [name, price]
    # p.append(name)
    # p.append(price)
    # products.append(p)
    # 下面寫法為上面 8 ~ 11 的簡寫法
    products.append([name, price])
    
print(products, "\n")
# print(products[0][0])

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 儲存檔案
with open('products.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
