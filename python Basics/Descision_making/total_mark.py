mark_1=int(input("enter the mark1 / 50: "))
mark_2=int(input("enter the mark2 / 50: "))
mark_3=int(input("enter the mark3 /50: "))

total=mark_1+mark_2+mark_3
percentage=2

total_mark=(percentage/100)*total


if(total>140):
    print("A")
elif(total>130 and total<=140):
    print("B")
elif(total>120 and total<=130):
    print("C")
else:
    print("Failed")
