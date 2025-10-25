angka = 1
while angka <= 5:
    print(angka)
    angka += 1

password = ""

while password != "123456789":
    password = input("Masukkan Password: ")
    if password != "123456789":
        print("Password salanh")

print("Berhasil")