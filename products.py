import os 

products = [] #大清單
if os.path.isfile('products.csv'): #檢查檔案在不在
    print('yeah 找到檔案！')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #繼續 跳到下一迴	
            name, price = line.strip().split(',')
            products.append([name,price])
    print(products)
else:
    print('找不到檔案...')


#讀取檔案
     

#讓使用者輸入
while True:
    name = input('輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入價格：')
    products.append([name,price]) 
print(products)

#印出所有購買記錄
for product in products:
    print(product[0], '價格是', product[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for product in products:
        f.write(product[0] + ',' + product[1] + '\n')