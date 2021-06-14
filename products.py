products = [] #大清單
while True:
    name = input('輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入價格：')
    products.append([name,price]) 
print(products)

for product in products:
    print(product[0], '價格是', product[1])