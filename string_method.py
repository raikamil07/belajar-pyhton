# name = input("masukkan nama anda: ")
phone_number = input("enter your phone number: ")

# result = len(name)
# result = name.rfind("a")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
result = phone_number.count("-")
phone_number = phone_number.replace("-", "")

print(phone_number)