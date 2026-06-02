# create a function called biggest_odd that takes a string or numbers and return the biggest ord_numbet in the list for example if you pass 23569 as an argument your function should return 9 use list comphrehension

def biggest_odd(value):
    odd_nums=[int(digit )for digit in str(value) if int(digit)%2!=0]
    return max(odd_nums)

print(biggest_odd(2369))