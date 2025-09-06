e = ["nilai1", 20, 3.14, False]
print(e)
print(e[1])
print(e[3])
print(e[-2])
print(e[-1])

f = ["raihan", ["belajar", "python"], 20, 3.14, ["nilai1", "nilai2"]]
print(f)
print(f[0])
print(f[1][0])
print(f[1][1])

f.append("tambahan")
print(f)

f.insert(3, 4.5)
print(f)

f.extend([70, 80, "hello"])
print(f)

f[0] = "kamil"
f[3] = 5.5
print(f)

# Menghapus elemen berdasarkan indeks
del f[2]
# Menghapus elemen berdasarkan nilai
f.remove("hello")
print(f)

#cari elemen
print(f.index('kamil'))

f.clear()
print(f)