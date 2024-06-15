# Definisikan kelas "Mahasiswa"
class Mahasiswa:
  def __init__(self, nama, nim, jurusan):
    self.nama = nama
    self.nim = nim
    self.jurusan = jurusan

  def tampilkan_profil(self):
    print(f"Nama: {self.nama}")
    print(f"NIM: {self.nim}")
    print(f"Jurusan: {self.jurusan}")

  def ubah_jurusan(self, jurusan_baru):
    self.jurusan = jurusan_baru

# Buat objek "mahasiswa1" dari kelas "Mahasiswa"
mahasiswa1 = Mahasiswa("John Doe", "123456", "Teknik Informatika")

# Tampilkan profil mahasiswa1
mahasiswa1.tampilkan_profil()

# Ubah jurusan mahasiswa1
mahasiswa1.ubah_jurusan("Sistem Informasi")

# Tampilkan profil mahasiswa1 lagi
mahasiswa1.tampilkan_profil()
