"""
Create a program that:
Takes student name
Takes course fee
Takes amount paid
Raise error if:
Fee is negative
Paid amount is negative
Paid amount is greater than fee
Handle invalid input
Always print "Registration Process Finished" using finally


"""
try:
    student_name= input("enter  student name:")
    course_fee = int(input("enter the course fee : "))
    amount_paid=int(input("enter the amount: paid"))
    if course_fee<0:
        raise Exception("fees is negative")
    if amount_paid <0:
        raise Exception ("paid amount  is negative")
    if amount_paid> course_fee:
        raise Exception("paid amount is grater than fee")
    
except Exception as e:
    print("e")

finally:
    print("registration successfull")