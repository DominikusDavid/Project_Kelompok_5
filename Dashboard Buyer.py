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
            KodePerusahaan.append(Kode)
            JumlahPembelian = int(input("Jumlah Pembelian: "))
            while(JumlahPembelian>JumlahUang):
                print("Jumlah Pembelian Invalid!")
                JumlahPembelian = int(input("Jumlah Pembelian: "))
            LembarSaham = JumlahPembelian/HargaSaham
            sumLembarSaham.append(LembarSaham)
        JumlahUang -= JumlahPembelian
        print(f"Sisa Uang: {JumlahUang}\n"
              f"Saham yang dipunya: {KodePerusahaan}\n"
              f"Jumlah lembar saham yang dipunya: {sumLembarSaham}\n")
        print(f"\n{Dashboard}")
        InputBuyer = str(input())
        