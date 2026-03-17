month=input("enter month: ")
match month:
    case "january" | "march" | "may" | "july" | "august" | "october" | "december":
        print("31 days")
    case "april" | "june" | "september" | "november":
        print("30 days")
    case "february":
        print("28 or 29 days")
    case _:
        print("Invalid month name")