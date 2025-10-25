# angka = int(input("massukkan input: "))

# if angka > 0:
#     print("Angka positif")

# if angka < 0:
#     print("Angka negatif")

# if angka == 0:
#     print("Angka adalah 0")

# nilai = int(input("Masukkan NIlai: "))

# if nilai >= 70:
#     print("anda lulus")
# else:
#     print("anda tidak lulus")

# nilai = int(input("Masukkan NIlai: "))

# if nilai >= 90:
#     print("nilai A")
# elif nilai >= 80:
#     print("Nilai B")
# elif nilai >= 70:
#     print("Nilai C")
# elif nilai >= 60:
#     print("Nilai D")
# else:
#     print("Nilai E")

# umur = int(input("Masukkan Umur: "))
# punya_sim = input("Apakah punya SIM(ya/tidak): ")

# if umur >= 17 and punya_sim == "ya":
#     print("anda bisa memakai motor")
# else:
#     print("Anda tidak boleh pakai motor")

# username = input("Masukkan Username: ")
# password = input("Masukkan Password: ")

# if username == "admin":
#     if password == "12345678":
#         print("Login Berhasil")
#         print("Selamat Datang Admin")
#     else:
#         print("Password Salah")
# else:
#     print("Username tidak ditemukkan")

# hari = input("Masukkan hari: ").lower()

# match hari:
#     case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
#         print("hari kerja")
#     case "sabtu" | "minggu":
#         print("hari libur")
#     case _:
#         print("hari tidak valid")

# if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
#     print("Hari kerja")
# elif hari == "sabtu" or hari == "minggu":
#     print("Hari libur")
# else:
#     print("Nama hari tidak valid/ada")

angka = int(input("Masukkan Angka: "))

hasil ="positif" if angka > 0 else "negatif"
print(hasil)