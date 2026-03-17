"""
dictionary contain key value pairs.
accessing the value using keys


expenses=[100,200,300]
            0   1   2



dictionary={key:value,key:value,................................}

"""
mobile={"brand":"apple","name":"iphone 17 pro max","ram":"256GB","price":175000} 


# accessing value
print(mobile["name"])
print(mobile["price"])

# updating value
mobile["price"]=180000
print(mobile)

"""
create a dictionary of a product with attribute
id,tittle,price ,avail_qty
"""

book={"id":1,"tittle":"alice in wonderland","price":250,"avail_qty":25}
print(book)
print(book["tittle"])
book["avail_qty"]+=25
print(book)

book["code"]="sku125"
print(book)

#  chk the key exist

if "offer" in book:
    print("yes")
else:
    print("no")

