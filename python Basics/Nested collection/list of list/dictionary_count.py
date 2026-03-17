orders={"tea":15,"coffee":21,"dosa":34,"rice":67}
order_lsit=[[v,k] for k,v in orders.items()]
print(sorted(order_lsit,reverse=True))