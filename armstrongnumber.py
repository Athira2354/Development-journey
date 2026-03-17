def is_armstrong(n):
    
    num=n
    digits=len(str(n))
    total=0
    while n>0:
        digit=n%10
        total+=digit**digits
        n//=10
        if total==num:
            print(num,"is_armstrong")
           
        else:
            
            print(num,"is not armstrong")
        
       
print(is_armstrong(153))
