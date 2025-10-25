age = int(input("masukkan umur anda: "))

if age >= 100:
    print("wah, anda sudah sangat tua")
elif age >= 18:
    print("anda sekarang legal")
elif age < 0:
    print("kamu belum lahir")
else:
    print("anda tidak legal, kamu harus 18+")