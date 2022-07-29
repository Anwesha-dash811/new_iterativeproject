products=[
{
    'productId':1,
    'productName':'Iphone13',
    'price':45678
},
{
    'productId':4,
    'productName':'Oneplus',
    'price':34987
},
{
    'productId':5,
    'productName':'SamsungGalaxy',
    'price':55987
},
]
a=len(products)
for i in range(0,a):
    if products[i]["price"]>=40000.0:
        print(products[i])
#list(filter(lambda product: product['price']>=40000,products))
