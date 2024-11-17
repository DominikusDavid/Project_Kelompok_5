# Meminta input ID pengguna
user_id = input("Masukkan ID Anda : ")

# Meminta input nomor pengguna
user_number = int(input("Masukkan Nomor Anda : "))

print(f"Welcome back {user_id}")

total_balance = 0  # Saldo total pengguna
stock_codes = []  # Daftar kode saham
stock_prices = []  # Daftar harga saham
stock_quantities = []  # Daftar jumlah lembar saham yang dibeli
buyer_portfolio = []

# Memeriksa jenis pengguna berdasarkan ID
if "#" in user_id: 
    dashboard = str("Dashboard Pembeli\n"
                    "Pilih salah satu\n"
                    "1. Topup\n"
                    "2. Pembelian\n"
                    "3. Lihat Portofolio\n"
                    "4. Cancel")
    
    print(dashboard)
    user_choice = input("Pilih Menu: ")   

    while user_choice != "4":
        if user_choice == "1":
            # Proses topup saldo
            topup_amount = int(input("Input Jumlah Topup: "))
            while topup_amount < 10000000:
                print("Jumlah Invalid! Topup tidak bisa kurang dari 10 juta")
                topup_amount = int(input("Input Jumlah Topup: "))
            total_balance += topup_amount
        
            print(f"Saldo Akhir: {total_balance}")
            print(dashboard)
            user_choice = input("Pilih Menu: ")

        elif user_choice == "2":
            # Proses pembelian saham
            if not stock_codes:  # Cek jika tidak ada saham yang tersedia
                print("Tidak ada saham yang tersedia untuk dibeli.")
            else:
                print("Daftar Kode Saham yang Tersedia:")
                for i in range(len(stock_codes)):
                    print(f"{stock_codes[i]}: {stock_prices[i]} per lembar")
                
                stock_code = input("Input Kode Saham yang ingin dibeli: ")
                
                if stock_code in stock_codes:
                    index = stock_codes.index(stock_code)
                    price_per_share = stock_prices[index]  # Ambil harga saham berdasarkan kode
                    print(f"Harga per lembar untuk {stock_code} adalah {price_per_share}")
                    
                    quantity_to_buy = int(input("Jumlah Lembar yang ingin dibeli: "))
                    total_cost = quantity_to_buy * price_per_share
                    
                    if total_cost > total_balance:
                        print("Saldo tidak cukup untuk melakukan pembelian!")
                    else:
                        # Update saldo dan jumlah lembar saham yang dibeli
                        total_balance -= total_cost
                        stock_quantities[index] += quantity_to_buy  # Update jumlah lembar saham yang dibeli
                        
                        print(f"Pembelian berhasil! Sisa Saldo: {total_balance}")
                else:
                    print("Kode saham tidak tersedia. Coba lagi.")
        
            print(dashboard)
            user_choice = input("Pilih Menu: ")

        elif user_choice == "3":
            # Menampilkan portofolio akhir
            print("Portofolio Akhir:")
            for i in range(len(stock_codes)):
                if stock_quantities[i] > 0:  # Hanya tampilkan saham yang dimiliki
                    print(f"{stock_codes[i]}: {stock_quantities[i]} lembar")
            print(dashboard)
            user_choice = input("Pilih Menu: ")

    # Simpan portofolio pembeli untuk digunakan oleh penjual
    buyer_portfolio = stock_quantities.copy()

elif "*" in user_id:
    # Dashboard Penjual
    dashboard_seller = ("Dashboard Penjual\n"
                         "Pilih salah satu\n"
                         "1. Penjualan\n"
                         "2. Portofolio\n"
                         "3. Cancel")
    
    seller_choice = 0
    while seller_choice != 3:
        print(dashboard_seller)
        seller_choice = int(input("Pilih salah satu: "))
        
        if seller_choice == 1:
            # Menampilkan portofolio pembeli untuk penjual
            print("Portofolio Pembeli:")
            for i in range(len(stock_codes)):
                if buyer_portfolio[i] > 0:  # Hanya tampilkan saham yang dimiliki
                    print(f"{stock_codes[i]}: {buyer_portfolio[i]} lembar")
            
            stock_code_to_sell = input("Masukkan kode saham yang ingin dijual: ")
            if stock_code_to_sell in stock_codes:
                index = stock_codes.index(stock_code_to_sell)
                if buyer_portfolio[index] > 0:
                    quantity_to_sell = int(input("Jumlah L embar yang ingin dijual: "))
                    if quantity_to_sell <= buyer_portfolio[index]:
                        sale_amount = quantity_to_sell * stock_prices[index]
                        total_balance += sale_amount
                        buyer_portfolio[index] -= quantity_to_sell
                        print(f"Penjualan berhasil! Sisa Saldo: {total_balance}")
                        print(f"Jumlah lembar saham {stock_code_to_sell} yang tersisa: {buyer_portfolio[index]}")
                    else:
                        print("Jumlah yang ingin dijual melebihi jumlah yang dimiliki.")
                else:
                    print("Anda tidak memiliki saham ini.")
            else:
                print("Kode saham tidak tersedia. Coba lagi.")

        elif seller_choice == 2:
            # Menampilkan portofolio penjual
            print("Portofolio Anda:")
            for i in range(len(stock_codes)):
                if buyer_portfolio[i] > 0:  # Hanya tampilkan saham yang dimiliki
                    print(f"{stock_codes[i]}: {buyer_portfolio[i]} lembar")

elif "%" in user_id: 
    # Input untuk menambahkan perusahaan IPO
    num_stocks = int(input("Masukkan jumlah perusahaan IPO: "))
    for i in range(num_stocks):
        stock_code = input("Masukkan Kode Perusahaan (awalan $): ")
        while not stock_code.startswith("$"):
            print("Masukkan kode perusahaan dengan awalan $")
            stock_code = input("Masukkan Kode Perusahaan (awalan $): ")
        
        stock_codes.append(stock_code)
        price_per_share = int(input(f"Harga saham per lembar untuk {stock_code}: "))
        stock_prices.append(price_per_share)
        stock_quantities.append(0)  # Inisialisasi jumlah lembar saham yang dibeli dengan 0

    print("Perusahaan IPO berhasil ditambahkan.")

    # Dashboard Pembeli
    dashboard = str("Dashboard Pembeli\n"
                    "Pilih salah satu\n"
                    "1. Topup\n"
                    "2. Pembelian\n"
                    "3. Lihat Portofolio\n"
                    "4. Cancel")
    
    print(dashboard)
    user_choice = input("Pilih Menu: ")   

    while user_choice != "4":
        if user_choice == "1":
            # Proses topup saldo
            topup_amount = int(input("Input Jumlah Topup: "))
            while topup_amount < 10000000:
                print("Jumlah Invalid! Topup tidak bisa kurang dari 10 juta")
                topup_amount = int(input("Input Jumlah Topup: "))
            total_balance += topup_amount
        
            print(f"Saldo Akhir: {total_balance}")
            print(dashboard)
            user_choice = input("Pilih Menu: ")

        elif user_choice == "2":
            # Proses pembelian saham
            if not stock_codes:  # Cek jika tidak ada saham yang tersedia
                print("Tidak ada saham yang tersedia untuk dibeli.")
            else:
                print("Daftar Kode Saham yang Tersedia:")
                for i in range(len(stock_codes)):
                    print(f"{stock_codes[i]}: {stock_prices[i]} per lembar")
                
                stock_code = input("Input Kode Saham yang ingin dibeli: ")
                
                if stock_code in stock_codes:
                    index = stock_codes.index(stock_code)
                    price_per_share = stock_prices[index]  # Ambil harga saham berdasarkan kode
                    print(f"Harga per lembar untuk {stock_code} adalah {price_per_share}")
                    
                    quantity_to_buy = int(input("Jumlah Lembar yang ingin dibeli: "))
                    total_cost = quantity_to_buy * price_per_share
                    
                    if total_cost > total_balance:
                        print("Saldo tidak cukup untuk melakukan pembelian!")
                    else:
                        # Update saldo dan jumlah lembar saham yang dibeli
                        total_balance -= total_cost
                        stock_quantities[index] += quantity_to_buy  # Update jumlah lembar saham yang dibeli
                        
                        print(f"Pembelian berhasil! Sisa Saldo: {total_balance}")
                        print(f"Jumlah lembar saham {stock_code} yang dimiliki: {stock_quantities[index]}")
                else:
                    print("Kode saham tidak tersedia. Coba lagi.")
        
            print(dashboard)
            user_choice = input("Pilih Menu: ")

        elif user_choice == "3":
            # Menampilkan portofolio akhir
            print("Portofolio Akhir:")
            for i in range(len(stock_codes)):
                if stock_quantities[i] > 0:  # Hanya tampilkan saham yang dimiliki
                    print(f"{stock_codes[i]}: {stock_quantities[i]} lembar")
            print(dashboard)
            user_choice = input("Pilih Menu: ")

    # Dashboard Penjual
    dashboard_seller = ("Dashboard Penjual\n"
                         "Pilih salah satu\n"
                         "1. Penjualan\n"
                         "2. Portofolio\n"
                         "3. Cancel")
    seller_choice = 0
    while seller_choice != 3:
        print(dashboard_seller)
        seller_choice = int(input("Pilih salah satu: "))
        
        if seller_choice == 1:
            # Menampilkan portofolio pembeli untuk penjual
            print("Portofolio Pembeli:")
            for i in range(len(stock_codes)):
                if stock_quantities[i] > 0:  # Hanya tampilkan saham yang dimiliki
                    print(f"{stock_codes[i]}: {stock_quantities[i]} lembar")
            
            stock_code_to_sell = input("Masukkan kode saham yang ingin dijual: ")
            if stock_code_to_sell in stock_codes:
                index = stock_codes.index(stock_code_to_sell)
                if stock_quantities[index] > 0:
                    quantity_to_sell = int(input("Jumlah Lembar yang ingin dijual: "))
                    if quantity_to_sell <= stock_quantities[index]:
                        sale_amount = quantity_to_sell * stock_prices[index]
                        total_balance += sale_amount
                        stock_quantities[index] -= quantity_to_sell
                        print(f"Penjualan berhasil! Sisa Saldo: {total_balance}")
                        print(f"Jumlah lembar saham {stock_code_to_sell} yang tersisa: {stock_quantities[index]}")
                    else:
                        print("Jumlah yang ingin dijual melebihi jumlah yang dimiliki.")
                else:
                    print("Anda tidak memiliki saham ini.")
            else:
                print("Kode saham tidak tersedia. Coba lagi.")

        elif seller_choice == 2:
            # Menampilkan portofolio penjual
            print("Portofolio Anda:")
            for i in range(len(stock_codes)):
                if stock_quantities[i] > 0:  # Hanya tampilkan saham yang dimiliki
                    print(f"{stock_codes[i]}: {stock_quantities[i]} lembar")

