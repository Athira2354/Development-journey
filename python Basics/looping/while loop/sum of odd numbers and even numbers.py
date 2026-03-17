

limit= int(input("enter limit"))

i=1

even_sum=0

odd_sum=0

while(i<=limit):
    if(i%2==0):
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
    i+=1
print("sum of",limit,"=",odd_sum)
print("sum of",limit,"=",even_sum)

