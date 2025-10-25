rows = int(input("Masukkan jumlah baris: "))
collumns = int(input("Masukkan jumlah kolom: "))
symbol = input("Masukkan simbol yang diinginkan: ")

for x in range(rows):
    for y in range(collumns):
        print(symbol, end="")
    print()

# for x in range(1, 6):
#     for y in range(x):
#         print(f"{x:^2}", end="")
#     print()