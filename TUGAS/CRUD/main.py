data = []

def cari_data(id):
    for d in data:
        if d["id"] == id:
            return d
    return None


def tambah_data():
    print("\nTambah Data")
    id = int(input("ID: "))
    if cari_data(id):
        print("ID sudah ada")
        return

    data.append({
        "id": id,
        "nama": input("Nama: "),
        "kelas": input("Kelas: ")
    })
    print("Data ditambah")


def tampil_data():
    print("\nData Siswa")
    if not data:
        print("Data kosong")
        return

    print("ID | Nama | Kelas")
    for d in data:
        print(d["id"], "|", d["nama"], "|", d["kelas"])


def ubah_data():
    print("\nUbah Data")
    id = int(input("ID: "))
    d = cari_data(id)

    if not d:
        print("Data tidak ditemukan")
        return

    d["nama"] = input("Nama baru: ")
    d["kelas"] = input("Kelas baru: ")
    print("Data diubah")


def hapus_data():
    print("\nHapus Data")
    id = int(input("ID: "))
    d = cari_data(id)

    if not d:
        print("Data tidak ditemukan")
        return

    data.remove(d)
    print("Data dihapus")


while True:
    print("\n1. Tambah")
    print("2. Tampil")
    print("3. Ubah")
    print("4. Hapus")
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
        break
    else:
        print("Menu tidak ada")
