print("Welcome to temperature converter")

unit = input("is this temparatue in celcius or fahrenheit (C/F): ")
temp = float(input("enter the temperature: "))

if unit == "C":
    temp = round((temp * 9/5) + 32)
    print(f"the temperature is {temp} F")
elif unit == "F":
    temp = round(5/9 * (temp - 32))
    print(f"the temperature is {temp} C")
else:
    print("invalid unit")