triangle=input("enter the type of triangle :")
match triangle:
    case "e":
        print("equilateral")
    case "i":
        print("isosceles")
    case "s":
        print("scalene")
    case _:
        print("undefined")