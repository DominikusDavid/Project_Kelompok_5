Nama = str(input("Masukkan ID Anda : "))

IDCard = int(input("Masukkan Nomor Anda : "))

print(f"Welcome back {Nama}")
if "#" in Nama: 
    #Dashboard Buyer
    JumlahUang = 0
    KodePerusahaan = []
    sumLembarSaham = []
    HargaSaham = 1 #Asumsi Harga saham semua perusahaan = 1 karena disini tidak ada data harga saham
    LembarSaham = 0

    Dashboard = str("Dashboard Buyer\n"
                    "Pilih salah satu\n"
                    "1. Topup\n"
                    "2. Pembelian\n"
                    "3. Cancel")
    
    print(Dashboard)
    InputBuyer = str(input())   

    while(InputBuyer != "3"):
        if(InputBuyer == "1"):
            JumlahPembelian = int(input("Input Jumlah Topup: "))
            while(JumlahPembelian<10000000):
                print("Jumlah Invalid! Topup tidak bisa kurang dari 10 juta")
                JumlahPembelian = int(input("Input Jumlah Topup: "))
            JumlahUang += JumlahPembelian
        
            print(f"Saldo Akhir: {JumlahUang}")
            print(Dashboard)
            InputBuyer = str(input())
    
        elif(InputBuyer == "2"):
            print(f"Saldo: {JumlahUang}")
            print("Tidak tersedia perusahaan IPO")
            break

elif "*" in Nama :
    DashboardS = ("Dashboard Seller\n"
                "Pilih salah satu\n"
                "1. Penjualan\n"
                "2. Portofolio\n"
                "3. Cancel")
    InputSeller = str(input("Pilih salah satu: "))
    while(InputSeller != 3):
        if (InputSeller == 1):
            KodePerusahaanS = str(input("Masukkan kode perusahaan : "))

            
elif "%" in Nama :  

    kodePerusahaanArr = []
    jumlahPerusahaan = int(input("Masukkan jumlah perusahaan IPO: "))
    i = 0

    while i < jumlahPerusahaan:

        KodePerusahaan = str(input("Masukkan Kode Perusahaan: "))

        if "$" in KodePerusahaan:
            kodePerusahaanArr.append(KodePerusahaan)
            i += 1

        elif "$" in KodePerusahaan:
            print("Masukkan kodePerusahaan dengan awalan $")

        else : pass

    for j in range(len(kodePerusahaanArr)):

        industriPerusahaanArr = []
        hargaIPOArr = []
        volumeIPOArr = []

        print("Masukkan detail untuk kode perusahaan : ", kodePerusahaanArr[j])
        
        industriPerusahaan = str(input("Asal Industri Perusahaan: "))
        industriPerusahaanArr.append(industriPerusahaan)

        hargaIPO = int(input("Harga saham per lembar (tanpa tanda baca): "))
        hargaIPOArr.append(hargaIPO)
        
        volumeIPO = int(input("Masukkan jumlah lembar saham IPO: "))
        volumeIPOArr.append(volumeIPO)

    #Dashboard Buyer
    JumlahUang = 0
    sumLembarSaham = []
    HargaSaham = 1 #Asumsi Harga saham semua perusahaan = 1 karena disini tidak ada data harga saham
    LembarSaham = 0
    KodePerusahaanBeli = []

    JumlahUang = 0
    hargaIPO = 1000000  # Contoh harga IPO
    sumLembarSaham = [0] * len(kodePerusahaanArr)  # Jumlah lembar saham per perusahaan
    KodePerusahaanBeli = []  # Daftar kode perusahaan yang dibeli

    # Menampilkan dashboard
    Dashboard = str("Dashboard Buyer\n"
                    "Pilih salah satu\n"
                    "1. Topup\n"
                    "2. Pembelian\n"
                    "3. Cancel")

    print(Dashboard)
    InputBuyer = input("Pilih Menu: ")

    while InputBuyer != "3":
        if InputBuyer == "1":
            JumlahPembelian = int(input("Input Jumlah Topup: "))
            while JumlahPembelian < 10000000:
                print("Jumlah Invalid! Topup tidak bisa kurang dari 10 juta")
                JumlahPembelian = int(input("Input Jumlah Topup: "))
            JumlahUang += JumlahPembelian
        
            print(f"Saldo Akhir: {JumlahUang}")
            print(Dashboard)
            InputBuyer = input("Pilih Menu: ")

        elif InputBuyer == "2":
            while True:
                print(f"Saldo: {JumlahUang}")
                Kode = input("Input Kode Perusahaan: ")
            
                if Kode in kodePerusahaanArr:
                    index = kodePerusahaanArr.index(Kode)
                    JumlahPembelian = int(input("Jumlah Pembelian: "))
                    while JumlahPembelian > JumlahUang:
                        print("Jumlah Pembelian Invalid!")
                        JumlahPembelian = int(input("Jumlah Pembelian: "))
                
                    LembarSaham = JumlahPembelian / hargaIPO
                    sumLembarSaham[index] += LembarSaham
                    KodePerusahaanBeli.append(Kode)
                
                    JumlahUang -= JumlahPembelian
                    print(f"Sisa Uang: {JumlahUang}\n"
                        f"Saham yang dipunya: {str(KodePerusahaanBeli)}\n"
                        f"Jumlah lembar saham yang dipunya: {sumLembarSaham}\n")
                    break  # Keluar dari loop setelah pembelian berhasil
                else:
                    print("Masukkan kode perusahaan yang tersedia. Coba lagi.")
        
            print(Dashboard)
            InputBuyer = input("Pilih Menu: ")

    DashboardS = ("Dashboard Seller\n"
            "Pilih salah satu\n"
            "1. Penjualan\n"
            "2. Portofolio\n"
            "3. Cancel")

    InputSeller = str(input("Pilih salah satu: "))

    while(InputSeller != 3):
        if (InputSeller == 1):
            KodePerusahaanS = str(input("Masukkan kode perusahaan : "))

            if (KodePerusahaanS in KodePerusahaanBeli):
                lembarDijual = int(input("Masukkan lembar yang akan dijual: "))
                if(lembarDijual > LembarSaham):
                    print("Lembar saham tak cukup")
                elif(lembarDijual < LembarSaham):
                    lembarDijualS = LembarSaham - lembarDijual
                else : 
                    lembarDijualS = 0
            
            elif (KodePerusahaanS not in KodePerusahaanBeli):
                print("Kamu tidak memiliki saham perusahan tersebut!")
            


                    
else : pass