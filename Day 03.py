# Dapatkan input dari pengguna
user_input = input("Masukkan nilai: ")

# Cek apakah input adalah integer
try:
    int(user_input)
    print("Tipe data tersebut adalah integer.")
except ValueError:
    # Jika tidak, cek apakah input adalah string
    if user_input.strip().replace(" ", "").isalpha():
        print("Tipe data tersebut adalah string.")
    else:
        print("Tipe data tersebut bukan integer atau string.")
