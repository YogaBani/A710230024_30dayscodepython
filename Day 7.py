class Mobil:
    def __init__(self, warna, tahun_keluaran, merk=None, model=None):
        self.warna = warna
        self.tahun_keluaran = tahun_keluaran
        self.merk = merk
        self.model = model

    def __str__(self):
        return f"Mobil {self.merk} {self.model} {self.warna} tahun {self.tahun_keluaran}"

# Example usage:
mobil1 = Mobil("Merah", 2015, "Toyota", "Corolla")
print(mobil1)  # Output: Mobil Toyota Corolla Merah tahun 2015

mobil2 = Mobil("Biru", 2020, "Honda", "Civic")
print(mobil2)  # Output: Mobil Honda Civic Biru tahun 2020
