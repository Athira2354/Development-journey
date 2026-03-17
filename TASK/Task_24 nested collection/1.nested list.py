products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]
"""
1. display all product names
2. product with the highest price
3. display electronics products
4. display products where the brand is Apple
5. which category has most products
6. product with maximum stock
7. list all categories

"""
# 1. display all product names
print(products)
product_names=[lst[1] for lst in products]
print(product_names)

# product with the highest price
max_price_product=products[0]
max_price_product=[lst[4] for lst in products if lst[4]>max_price_product[4]]
max_price_product=products
print(f'Highest Price Product:", {max_price_product[1]}')

# 3. display electronics products
electronic_products=products[3]
electronic_products=[lst[1] for lst in products if lst[3]=="Electronics"]
print(f'electronics_products={electronic_products}')

# 4. display products where the brand is Apple
product_brand=products[2]
brand=[lst[1] for lst in products if lst[2]=="Apple"]
print(f'products in apple_brand={product_brand}')



# 5. which category has most products
all_categories=[p[3] for p in products]
category_count={c:all_categories.count(c) for c in all_categories}
c_count_list=[[v,k]for k,v in category_count.items()]
print(sorted(c_count_list,reverse=True))

# 6.product with maximum stock

max_stock = max([lst[5] for lst in products])
max_stock_product = [lst for lst in products if lst[5] == max_stock]
print(f"maximum stock=, {max_stock_product}")

# # 7. list all categories
unique_categories=list[set([lst[3] for lst in products])]
print(f'unique_categories={unique_categories}')
