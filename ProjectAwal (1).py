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
            
elif "*" in Nama :pass
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

    for j in kodePerusahaanArr:

        industriPerusahaanArr = []
        hargaIPOArr = []
        volumeIPOArr = []

        print("Berikan detail untuk kode perusahaan: ",kodePerusahaanArr[j])
        
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
            Kode = str(input("Input Kode Perusahaan: "))
        
            if(Kode in KodePerusahaan):
                for i in range(len(KodePerusahaan)):
                    if(Kode == KodePerusahaan[i]):
                        JumlahPembelian = int(input("Jumlah Pembelian: "))
                        while(JumlahPembelian>JumlahUang):
                            print("Jumlah Pembelian Invalid!")
                            JumlahPembelian = int(input("Jumlah Pembelian: "))
                        LembarSaham = JumlahPembelian/HargaSaham
                        sumLembarSaham[i] = sumLembarSaham[i] + LembarSaham
        
            elif(Kode not in KodePerusahaan):
                print("Masukkan kode perushaan yang tersedia")
                
            JumlahUang -= JumlahPembelian
            print(f"Sisa Uang: {JumlahUang}\n"
                f"Saham yang dipunya: {KodePerusahaan}\n"
                f"Jumlah lembar saham yang dipunya: {sumLembarSaham}\n")
            print(f"\n{Dashboard}")
            InputBuyer = str(input())
                    
else : pass
