# 6
# 1,2,3,4,5,6
# divisors=1,2,3
# sum(6)=1+2+3

number =6
sum=0
for i in range(1,number):
    if number%i==0:
        sum=sum + i


print("perfect number" if number==sum else "not a perfect number")

# if number==sum:
#     print(number,"is  a perfect number ")
# else:
#     print(number,"is  not a perfect number ")