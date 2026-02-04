data = []

def tambah_data():
    print("\nTambah Data")
    id = int(input("Masukkan id: "))
    nama = input("Masukkan nama: ")
    kelas = input("Masukkan kelas: ")

    for d in data:
        if d["id"] == id:
            print("ID sudah ada")
            return

    data.append({
        "id": id,
        "nama": nama,
        "kelas": kelas
    })

    print("Data berhasil ditambah")


def tampil_data():
    print("\nData Siswa")
    if len(data) == 0:
        print("Data masih kosong")
        return

    print("ID | Nama | Kelas")
    for d in data:
        print(d["id"], "|", d["nama"], "|", d["kelas"])


def ubah_data():
    print("\nUbah Data")
    id = int(input("Masukkan id yang mau diubah: "))

    ketemu = False
    for d in data:
        if d["id"] == id:
            d["nama"] = input("Nama baru: ")
            d["kelas"] = input("Kelas baru: ")
            print("Data berhasil diubah")
            ketemu = True

    if ketemu == False:
        print("Data tidak ditemukan")


def hapus_data():
    print("\nHapus Data")
    id = int(input("Masukkan id yang mau dihapus: "))

    for d in data:
        if d["id"] == id:
            data.remove(d)
            print("Data berhasil dihapus")
            return

    print("Data tidak ditemukan")


while True:
    print("\n=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        tambah_data()
    elif pilih == "2":
        tampil_data()
    elif pilih == "3":
        ubah_data()
    elif pilih == "4":
        hapus_data()
    elif pilih == "0":
        print("Keluar dari program")
        break
    else:
        print("Menu tidak ada")
