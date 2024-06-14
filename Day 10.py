class MobilListrik:
    def __init__(self, nama, kapasitas_baterai, jarak_tempuh_maksimal):
        self.nama = nama
        self.kapasitas_baterai = kapasitas_baterai
        self.jarak_tempuh_maksimal = jarak_tempuh_maksimal
        self.baterai_terisi = 0

    def isi_baterai(self, jumlah_isi):
        if self.baterai_terisi + jumlah_isi <= self.kapasitas_baterai:
            self.baterai_terisi += jumlah_isi
            print(f"Baterai {self.nama} telah diisi sebanyak {jumlah_isi} kWh. Kapasitas baterai saat ini adalah {self.baterai_terisi} kWh.")
        else:
            print(f"Baterai {self.nama} sudah penuh. Kapasitas baterai maksimal adalah {self.kapasitas_baterai} kWh.")

    def kurangi_baterai(self, jumlah_kurang):
        if self.baterai_terisi - jumlah_kurang >= 0:
            self.baterai_terisi -= jumlah_kurang
            print(f"Baterai {self.nama} telah dikurangi sebanyak {jumlah_kurang} kWh. Kapasitas baterai saat ini adalah {self.baterai_terisi} kWh.")
        else:
            print(f"Baterai {self.nama} tidak cukup untuk dikurangi sebanyak {jumlah_kurang} kWh.")

    def cek_jarak_tempuh(self):
        jarak_tempuh_saat_ini = self.baterai_terisi / self.kapasitas_baterai * self.jarak_tempuh_maksimal
        print(f"Mobil {self.nama} dapat menempuh jarak sebanyak {jarak_tempuh_saat_ini:.2f} km dengan baterai saat ini.")

# Contoh penggunaan
mobil1 = MobilListrik("Tesla Model 3", 75, 560)
mobil1.isi_baterai(50)
mobil1.cek_jarak_tempuh()
mobil1.kurangi_baterai(20)
mobil1.cek_jarak_tempuh()
