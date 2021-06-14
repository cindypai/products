import os 

#讀取檔案
def read_file(filename):
    products = [] #大清單
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #繼續 跳到下一迴    
            name, price = line.strip().split(',')
            products.append([name,price])
    return products    
     

#讓使用者輸入
def user_input(products):
    while True:
        name = input('輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入價格：')
        products.append([name,price]) 
    print(products)
    return products


#印出所有購買記錄
def print_products(products):
    for product in products:
        print(product[0], '價格是', product[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for product in products:
            f.write(product[0] + ',' + product[1] + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案在不在
        print('yeah 找到檔案！')
        products = read_file(filename)
    else:
        print('找不到檔案...')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()
