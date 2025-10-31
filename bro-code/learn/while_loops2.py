age = int(input("masukkan umur anda: "))

while age < 0:
    print("umur tidak valid")
    age = int(input("masukkan umur anda: "))
print(f"umur anda adalah: {age}")