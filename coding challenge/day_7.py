# write a function string_range that takes a single number and return a string of its range the string characters should be seperated by dots(.) for example if you pass 6 as an argument your functio should return '0.1.2.3.4.5'.
def string_range(num):
    result=[]
    for i in range(num):
        result.append(str(i))
    return ".".join(result)
number=int(input("enter a number :"))
print(string_range(number))