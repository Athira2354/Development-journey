# century year=10000
# to check whether an year is century year  check whether the input has atleast two zero at the end  if ther

year=int(input("enter a year :"))
if(year%100==0):
    print("century year")
else:
    print("non century year")