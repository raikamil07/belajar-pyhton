principle = 0
interest = 0
time = 0

while True:
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Principal amount must be greater than 0. Please try again.")
    else:
        break

while True:
    interest = float(input("Enter the annual interest rate: "))
    if interest < 0:
        print("Interest rate must be greater than 0. Please try again.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time must be greater than 0. Please try again.")
    else:
        break

total = principle * (1 + interest / 100) ** time
print(f"Balance after {time} year/s is: ${total:.2f}")

print(principle)
print(interest)
print(time)