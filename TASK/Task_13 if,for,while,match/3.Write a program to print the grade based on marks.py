"""
3. Write a program to print the grade based on marks:
* 90 and above → A
* 75–89 → B
* 50–74 → C
* Below 50 → Fail



"""
mark=int(input("enter the mark:"))
match mark:
    case _ if mark>=90:
        print("A grade")
    case _ if mark>=75 and mark<=89:
        print("B grade")
    case _ if mark>=50 and mark<=75:
        print("C grade")
    case _:
        print("failed")
