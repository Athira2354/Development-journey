def is_fibnocii(number):
    is_fib=False
    prev=0
    curr=1
    next=prev+curr
    while(next<number):
        next = prev+curr
        prev=curr
        curr=next
        if next==number:
            is_fib=True
            break

    return is_fib
print(is_fibnocii(9))
print(is_fibnocii(8))