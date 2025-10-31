class laptop:
    def __init__(self, merk, year, color, for_sale):
        self.barang = merk
        self.tahun = year
        self.warna = color
        self.di_jual = for_sale
    
    # attributes  
    def turn_on(self):
        print("Laptop goes on")
    
    def turn_off(self):
        print("Laptop goes off")

# Methods
laptop1 = laptop("Asus", 2025, "black", False)


print(laptop1)
