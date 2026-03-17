"""

match variable: syntax
    case1:
        stmt1
    case 2:
        stmt 2
        '
        '
        '
        '
    case_
        print("invalid)
"""

day=int(input("enter the day: "))

match day:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("Tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("saturday")
    case _ :
        print("invalid")
    
    