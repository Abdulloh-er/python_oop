class sistem:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def cek_password(self, password):
        return self.__password == password


class rekening:
    def __init__(self, nama_nasabah, sandi_nasabah):
        self.nama_nasabah = nama_nasabah
        self.__sandi_nasabah = sandi_nasabah
        self.saldo = 0

    def cek_sandi_nasabah(self, sandi):
        return self.__sandi_nasabah == sandi


class login(sistem):
    pass


data_akun = []
data_nasabah = []

while True:
    print("\n============= HOME =============")
    print("1. Register")
    print("2. Login")
    print("3. Quit")

    selection = input("PILIH 1-3 : ")


    if selection == "1":
        print("\n============= REGISTER =============")
        username = input("USERNAME : ")
        password = input("PASSWORD : ")

        akun_baru = login(username, password)
        data_akun.append(akun_baru)

        print("Akun berhasil dibuat!")

  
    elif selection == "2":
        print("\n============= LOGIN =============")
        username = input("USERNAME : ")
        password = input("PASSWORD : ")

        status_login = False

        for akun in data_akun:
            if akun.username == username:
                if akun.cek_password(password):
                    status_login = True
                    break

        if status_login:

            while True:
                print("\n============= MENU =============")
                print("1. Buat rekening")
                print("2. Cek rekening")
                print("3. Setor tunai")
                print("4. Tarik tunai")
                print("5. Logout")

                pilih = input("PILIH 1-5 : ")

           
                if pilih == "1":
                    nama = input("Nama nasabah : ")
                    sandi = input("Sandi nasabah : ")

                    rekening_baru = rekening(nama, sandi)
                    data_nasabah.append(rekening_baru)

                    print("Rekening berhasil dibuat!")

        
                elif pilih == "2":
                    nama = input("Nama nasabah : ")
                    sandi = input("Sandi nasabah : ")

                    ditemukan = False

                    for r in data_nasabah:
                        if r.nama_nasabah == nama:
                            if r.cek_sandi_nasabah(sandi):
                                print("===== DATA REKENING =====")
                                print("Nama :", r.nama_nasabah)
                                print("Saldo :", r.saldo)
                                ditemukan = True

                    if ditemukan == False:
                        print("Rekening tidak ditemukan!")

         
                elif pilih == "3":
                    nama = input("Nama nasabah : ")
                    sandi = input("Sandi nasabah : ")

                    for r in data_nasabah:
                        if r.nama_nasabah == nama:
                            if r.cek_sandi_nasabah(sandi):
                                jumlah = int(input("Jumlah setor : "))
                                r.saldo = r.saldo + jumlah
                                print("Setor berhasil!")

          
                elif pilih == "4":
                    nama = input("Nama nasabah : ")
                    sandi = input("Sandi nasabah : ")

                    for r in data_nasabah:
                        if r.nama_nasabah == nama:
                            if r.cek_sandi_nasabah(sandi):
                                jumlah = int(input("Jumlah tarik : "))
                                if jumlah > r.saldo:
                                    print("Saldo tidak cukup!")
                                else:
                                    r.saldo = r.saldo - jumlah
                                    print("Tarik berhasil!")

                elif pilih == "5":
                    print("Logout berhasil!")
                    break


                else:
                    print("Pilihan salah!")


        else:
            print("Login gagal!")





    elif selection == "3":
        print("Terima kasih.")
        break

    else:
        print("Pilihan salah!")
