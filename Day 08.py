# Open the file in read mode
file_puisi = open("puisi.txt", "r")

# Read the contents of the file
puisi = file_puisi.readlines()

# Print the contents of the file
for teks in puisi:
    print(teks)

# Close the file
file_puisi.close()

# Open the file in append mode
file_bio = open("biodata.txt", "a")

# Get user input
nama = input("Nama: ")
umur = int(input("Umur: "))
alamat = input("Alamat: ")

# Format the text
teks = "\nNama: {}\nUmur: {}\nAlamat: {}\n---".format(nama, umur, alamat)

# Write the text to the file
file_bio.write(teks)

# Close the file
file_bio.close()
