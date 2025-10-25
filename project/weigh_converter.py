print("Welcome to weight converter")

weight = float(input("enter your weight: "))
unit = input("kilogram or pound (K/P): ")

if unit == "K":
    weight = weight * 2.20462
    unit = "Lbs."
elif unit == "P":
    weight = weight / 2.205
    unit = "Kg."
else:
    print("invalid unit")

print(f"your weight is {weight} {unit}")