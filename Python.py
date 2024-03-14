# Data dictionary username dan password mahasiswa
data_mahasiswa = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10"
}

# Fungsi untuk proses login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Periksa kecocokan username dan password
    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print("Selamat datang,", username)
    else:
        print("Data yang dimasukkan salah.")

# Panggil fungsi login
login()