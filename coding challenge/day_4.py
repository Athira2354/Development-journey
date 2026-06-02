# write a function called only_float which takes two parameters a and b and return 2 if both arguments are float, return 1 if only on argument is float ,and return 0 if neither argument is float if you pass (12.1,13) as argument your function should return a 1

def only_float(a,b):

    if type(a)==float and type(b)==float :
        return 2
    elif type(a)==float or type(b)==float :
        return 1
    else:
        return 0
    
print(only_float(12.1,13))
    