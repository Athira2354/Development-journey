num=int(input("enter a number:"))

is_prime=False

for i in range(2,num):
    if(num%i==0):
        is_prime= True
        break
print(is_prime)