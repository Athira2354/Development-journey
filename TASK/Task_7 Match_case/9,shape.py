shape =input("enter the shape: ")
match shape:
    case "c":
        print("circle")
    case "r":
        print("rectangle")
    case "s":
        print("square")
    case _ :
        print("undefined shape")