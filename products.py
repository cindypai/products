products = [] #大清單
while True:
    name = input('輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入價格：')
    products.append([name,price]) 
print(products)

products[0][0]