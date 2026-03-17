lst=[10,20,30,40,50,60]
index=int(input("enter the index number :"))
try:
    print(lst[index])
except Exception as e:
    index=int(input("enter the number :"))
    print(lst[index])
finally:
    print("file operation................")
    print("db commit.................")


"""
custom error 
"""
age=int(input("enter the age: "))

if age<18:
    raise Exception("invalid age")
else:
    print("access granted")