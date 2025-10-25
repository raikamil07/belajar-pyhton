operator = input("masukkan operator (+, -, *, /): ")

num1 = float(input("masukkan angka pertama: "))
num2 = float(input("masukkan angka kedua: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result)}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result)}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {round(result)}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {round(result)}")
else:
    print(f"{operator} tidak valid")