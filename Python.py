data_mahasiswa = {
    "Johnny": "07352311165",
    "Kun": "07352311166",
    "Renjun": "07352311167",
    "Mark": "07352311168",
    "Taeyong": "07352311169",
    "Xiaojun": "07352311170",
    "Riku": "07352311171",
    "Sakuya": "07352311172",
    "yangyang": "07352311173",
    "Sion": "07352311174"
}

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print("Selamat datang,", username)
    else:
        print("Data yang dimasukkan salah.")

login()