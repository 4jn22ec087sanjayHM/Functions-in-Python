def create_product(name, price, quantity, category="Electronics"):
    return name,price,quantity,category
product1=create_product("lenovo",97800,3)
product2=create_product("HP",50000,5)
product3=create_product("Asus",120000,8,"mechanic")
print(product1)
print(product2)
print(product3)