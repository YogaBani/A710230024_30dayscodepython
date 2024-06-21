class Kucing:
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna
        self.pemilik = None

    def makan(self):
        print(f"{self.nama} sedang makan")

    def tidur(self):
        print(f"{self.nama} sedang tidur")

    def set_pemilik(self, pemilik):
        self.pemilik = pemilik

class Pemilik:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.kucing = []

    def tambah_kucing(self, kucing):
        self.kucing.append(kucing)
        kucing.set_pemilik(self)

    def lihat_kucing(self):
        for kucing in self.kucing:
            print(f"Nama kucing: {kucing.nama}, Umur: {kucing.umur}, Warna: {kucing.warna}")

# Create a cat
kucing1 = Kucing("Mimi", 2, "Putih")
kucing2 = Kucing("Nini", 3, "Hitam")

# Create an owner
pemilik1 = Pemilik("John", "Jalan Sudirman")

# Add the cat to the owner
pemilik1.tambah_kucing(kucing1)
pemilik1.tambah_kucing(kucing2)

# Print the owner's cats
pemilik1.lihat_kucing()
