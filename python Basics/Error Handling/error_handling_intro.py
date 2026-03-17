

"""
types of errors
----------------------------

 division by zero

 run time error

 file not found error

 index error

 key error
 --------------------------------
-----------error handling keyword--------------

try-----------------------|
except--------------------|----------Blocks
finally-------------------|



raise--------------|
                   |----------keywords
assert-------------|



syntax
-----------------
try:
    doubtfull code

except:

    handling code

finally :

    cleanup process


----------------------------------------------------------------

 raise() - keyword is used for creating custom error 


 assert()-
            assertion is used for debugging
            when the condition is failed  an ssertion message hits
 ---------------
 syntax
 ----------
 assert condition,"message

""" 

lst=[10,12,14,16,18,20]
index=int(input("enter the index position :"))
try:
    print(lst[index])
except Exception as e:
    print(e)
print("database commit")
print("database write")