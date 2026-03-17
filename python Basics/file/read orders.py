fr=open("python Basics\\file operations\\order.txt","r")
all_orders=[]
for line in fr:
    cleaned_data=line.rstrip("\n")
    all_orders.append(cleaned_data)
order_count={o:all_orders.count(o) for o in all_orders}
print(order_count)
