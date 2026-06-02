# Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount (percentage) of the product. Once the user inputs the price and discount, it calculates the price after the discount. The function should return the price after the discount. For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.



def discount():
    price= float(input("enter the price : "))
    discount_percentage= float(input("enter the percentage : "))
    after_discount_amount=(discount_percentage/100)*price
    final_price=price-after_discount_amount

    return final_price
print("price after discount = ",discount())
