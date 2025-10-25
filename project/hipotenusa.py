import math

a = float(input("masukkan panjang sisi alas segitiga: "))
b = float(input("masukkan panjang sisi tinggi segitiga: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"panjang sisi miring segitiga adalah: {round(c, 2)}")