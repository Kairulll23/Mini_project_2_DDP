# Nama : Khairul Ikhsan
# NIM  : 2509116097

# daftar pengguna
pengguna = {
    "khairul": {"password": "123", "role": "Manager"},
    "aldi": {"password": "123", "role": "Karyawan"}
}

# data karyawan
data_karyawan = []

# login
def login():
    while True:
        print("="*22)
        print("=== Selamat Datang ===")
        print("="*22)
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in pengguna and pengguna[username]["password"] == password:
            role = pengguna[username]["role"]
            print(f"\nSelamat datang {username}! Kamu berhasil login sebagai {role}.\n")
            return role
        else:
            print("Username atau password salah\n")

# tambah 
def tambah_karyawan():
    nama = input("Nama karyawan: ")
    jabatan = input("Jabatan karyawan: ")
    data_karyawan.append({"nama": nama, "jabatan": jabatan})
    print(f"karyawan '{nama}' sudah ditambahkan.")

# lihat
def lihat_karyawan():
    if not data_karyawan:
        print("Belum ada karyawan yang tersimpan.")
    else:
        print("\n--- Daftar Karyawan ---")
        for i, k in enumerate(data_karyawan, start=1):
            print(f"{i}. {k['nama']} - {k['jabatan']}")
        print("-"*25)

# update 
def update_karyawan():
    lihat_karyawan()
    try:
        id_pengguna = int(input("Pilih nomor karyawan yang mau diubah: ")) - 1
        if 0 <= id_pengguna < len(data_karyawan):
            nama = input("Nama baru: ")
            jabatan = input("Jabatan baru: ")
            data_karyawan[id_pengguna] = {"nama": nama, "jabatan": jabatan}
            print("berhasil diperbarui.")
        else:
            print("Betul aja kah ini?")
    except ValueError:
        print("Salah Cuyy")

# hapus 
def hapus_karyawan():
    lihat_karyawan()
    try:
        id_pengguna = int(input("Pilih nomor karyawan yang mau dihapus: ")) - 1
        if 0 <= id_pengguna < len(data_karyawan):
            terhapus = data_karyawan.pop(id_pengguna)
            print(f"Data karyawan '{terhapus['nama']}' sudah dihapus.")
        else:
            print("Betul aja kah ini?")
    except ValueError:
        print("Salah Cuyy")

# menu
def main():
    role = login()
    while True:
        print("\n=== Menu ===")
        print("1. Lihat karyawan")
        if role == "Manager":
            print("2. Tambah karyawan")
            print("3. Ubah data karyawan")
            print("4. Hapus karyawan")
            print("5. Keluar")
        else:
            print("2. Keluar")

        pilihan = input("Pilih menu (angka): ")

        if pilihan == "1":
            lihat_karyawan()
        elif pilihan == "2" and role == "Manager":
            tambah_karyawan()
        elif pilihan == "3" and role == "Manager":
            update_karyawan()
        elif pilihan == "4" and role == "Manager":
            hapus_karyawan()
        elif (pilihan == "5" and role == "Manager") or (pilihan == "2" and role != "Manager"):
            print("Done ga Bang (Done!!!)")
            break
        else:
            print("Salah Cuyy")

main()