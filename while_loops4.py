num = int(input("enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid please choose again")
    num = int(input("enter a number between 1 - 10: "))

print(f"you choose {num}")