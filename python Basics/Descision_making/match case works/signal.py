signal=input("enter the signal:")
match signal:
    case "Red":
        print("Stop")
    case "Green":
        print("Go")
    case "Yellow":
        print("Wait")
    case _:
        print("invalid")
