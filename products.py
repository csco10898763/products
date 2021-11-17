import os # operating system

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r') as f: 
        for line in f:
            if '商品,價格' in line:
                continue # 跳到下一次迴圈的意思
            name, price = line.strip().split(',') # strip() 去掉跳行符號 \n & 資料以 ',' 作為分割
            products.append([name, price])
        print(products)
    return products

# def read_file(filename):
#     products = []
#     if os.path.isfile(filename):  # 檢查檔案在不在
#         print('yeah !! 找到檔案了 !!\n')
#         with open(filename, 'r') as f: 
#             for line in f:
#                 if '商品,價格' in line:
#                     continue # 跳到下一次迴圈的意思
#                 name, price = line.strip().split(',') # strip() 去掉跳行符號 \n & 資料以 ',' 作為分割
#                 products.append([name, price])
#         print(products)
#     else:
#         print('找不到檔案 !!\n')
#     return products

# 讓使用者輸入
def user_input(products):
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
    return products
# print(products[0][0])

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 儲存檔案
def write_file(filename, products):
    with open(filename, 'w') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  # 檢查檔案在不在
        print('yeah !! 找到檔案了 !!\n')
        products = read_file(filename)
    else: 
        print('找不到檔案 !!\n')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()