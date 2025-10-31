def day_of_week(day):
    match day:
        case 1:
            return "its monday"
        case 2:
            return "its tuesday"
        case 3:
            return "its wendnesday"
        case 4:
            return "its thursday"
        case 5:
            return "its friday"
        case 6:
            return "its saturday"
        case 7:
            return "its sunday"
        case _:
            return "its not valid"
        
print(day_of_week(1))

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("sunday"))