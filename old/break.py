angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka antara 1-10: "))
    if tebakan == angka_rahasia:
        print("tebakan anda benar")
        break
    else:
        print("tebakan anda salah")