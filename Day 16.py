# harga_rumah.py

class Rumah:
    def __init__(self, alamat, harga, kamar_tidur, kamar_mandi, luas):
        self.alamat = alamat
        self.harga = harga
        self.kamar_tidur = kamar_tidur
        self.kamar_mandi = kamar_mandi
        self.luas = luas

    def __str__(self):
        return f"Rumah di {self.alamat}: Rp {self.harga:.2f}, {self.kamar_tidur} kamar tidur, {self.kamar_mandi} kamar mandi, {self.luas} m²"

class SistemHargaRumah:
    def __init__(self):
        self.rumah = []

    def tambah_rumah(self, rumah):
        self.rumah.append(rumah)

    def dapatkan_rumahs(self):
        return self.rumah

    def dapatkan_rata_rata_harga(self):
        total_harga = sum(rumah.harga for rumah in self.rumah)
        return total_harga / len(self.rumah)

    def dapatkan_rumah_termahal(self):
        return max(self.rumah, key=lambda x: x.harga)

    def dapatkan_rumah_termurah(self):
        return min(self.rumah, key=lambda x: x.harga)

    def cari_berdasarkan_alamat(self, alamat):
        for rumah in self.rumah:
            if rumah.alamat.lower() == alamat.lower():
                return rumah
        return None

# Contoh penggunaan:
sistem = SistemHargaRumah()

rumah1 = Rumah("Jl. Soekarno", 500000000, 3, 2, 150)
rumah2 = Rumah("Jl. Patimura", 300000000, 2, 1, 100)
rumah3 = Rumah("Jl. Slamet Riyadi", 700000000, 4, 3, 250)

sistem.tambah_rumah(rumah1)
sistem.tambah_rumah(rumah2)
sistem.tambah_rumah(rumah3)

print("Semua Rumah:")
for rumah in sistem.dapatkan_rumah():
    print(rumah)

print(f"\nRata-rata Harga: Rp {sistem.dapatkan_rata_rata_harga():.2f}")
print(f"Rumah Termahal: {sistem.dapatkan_rumah_termahal()}")
print(f"Rumah Termurah: {sistem.dapatkan_rumah_termurah()}")

print("\nCari Berdasarkan Alamat:")
alamat = input("Masukkan alamat: ")
hasil = sistem.cari_berdasarkan_alamat(alamat)
if hasil:
    print(hasil)
else:
    print("Rumah tidak ditemukan")
