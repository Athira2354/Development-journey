def max_two(num1,num2):
    result=1
    if num1>num2:
        return num1
    else:
        return num2
    return result
assert max_two(10,20)==10,"test case failed"
assert max_two(-5,5)==5,"testcase 2 failed"

print(" code accepted")
