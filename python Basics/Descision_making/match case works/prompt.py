prompt=input("enter the prompt:")
match prompt:
    case "START":
        print("System  starting>>>")
    case "STOP":
        print("System  Shutting down>>>")
    case "RESTART":
        print("System   Restarting>>>")
    case _:
        print("invalid prompt >>>")