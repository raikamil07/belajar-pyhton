nama = "Raihan"
umur = 18

pesan = "Hallo saya " + nama + ", umur saya " + str(umur)
print(pesan)

panjang_nama = len(nama)
panjang_pesan = len(pesan)

print(len(nama))
print(len(pesan))

nama = "python"
print(nama[0])
print(nama[1])
print(nama[2])

print(nama[-1])
print(nama[-2])
print(nama[-3])

nama = "python"
print(nama[:])
print(nama[3:5])
print(nama[1:4])

nama = "Alice"
print(nama)
nama_upper = nama.upper()
print(nama_upper)
nama_lower = nama.lower()
print(nama_lower)

nama = "raihan kamil"
nama_title = nama.title()
print(nama_title)
nama_capitalize = nama.capitalize()
print(nama_capitalize)

nama = "    raihan     "
nama_strip = nama.strip()
print(nama_strip)

kalimat = "i love fineshyt"
kalimat_replace = kalimat.replace("fineshyt", "raihan kamil")
print(kalimat_replace)

nama = "raihan kamil"
jumlah = nama.count("a")
print(jumlah)

kalimat = "fineshyt is so good at programing"
posisi = kalimat.find("programing")
print(posisi)

kalimat = "baris pertama\nbaris kedua"
print(kalimat)

kalimat = "Nama:\tRaihan\numur:\t18"
print(kalimat)

path = "C:\\newfolder\\raihan.txt"
print(path)

kalimat = "fineshyt mengatakan \"hello\" kepada saya"
print(kalimat)

nama = "raihan kamil"
umur = 18
kota = "Bandung"

profil = f"Nama saya {nama}, umur saya {umur}, saya tinggal di {kota}"
print(profil)

harga = 15000
jumlah = 5
total = f"harga {harga} x {jumlah} = {harga * jumlah}"
print(total)