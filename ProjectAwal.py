Nama = str(input("Masukkan ID Anda : "))

IDCard = int(input("Masukkan Nomor Anda : "))

print(f"Welcome back {Nama}")
if "#" in Nama: pass
elif "*" in Nama : pass
elif "%" in Nama :  

    kodePerusahaanArr = []
    jumlahPerusahaan = int(input("Masukkan jumlah perusahaan IPO: "))
    i = 0

    while i < jumlahPerusahaan:

        kodePerusahaan = str(input(""))

        if "$" in kodePerusahaan:
            kodePerusahaanArr.append(kodePerusahaan)
            i += 1

        elif "$" in kodePerusahaan:
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
        
else : pass
