num1=int(input("enter number 1:"))

num2=int(input("enter number 2:"))

if(num1<num2):
    smallest=num1
else:
    smallest=num2

gcd=1

for i in range(1,smallest+1):
    if num1 % i==0 and num2%i==0:
        gcd=i
print(gcd)