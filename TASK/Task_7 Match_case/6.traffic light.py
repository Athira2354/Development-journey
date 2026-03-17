traffic_light=input("enter the traffic light color:")
match traffic_light:
    case "red":
        print("stop")
    case "green":
        print("Pass")
    case "yellow":
        print("Wait")
    case _ :
        print("undefined")