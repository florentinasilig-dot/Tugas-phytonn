while True:
    print("\nmenu pilihan")
    print("1. Barisan Fibonacci")
    print("2. M Kali N")
    print("0. Keluar")
    
    pilihan = int(input("Pilih Menu : "))
    
    if pilihan == 1:
        n = int(input("Masukkan Jumlah Suku : "))
        a, b = 1, 1
        print(f"barisan fibonacci sebanyak {n} suku :")
        for i in range(n):
            print(a, end=", " if i != n-1 else "\n")
            a, b = b, a + b
            
    elif pilihan == 2:
        m = int(input("Masukkan Suatu Bilangan Bulat : "))
        n = int(input("Masukkan Suatu Bilangan Pengali : "))
        hasil = m * n
        print(f"{m} x {n} = {hasil}")
        
    elif pilihan == 0:
        print("Program selesai.")
        break
        
    else:
        print("Pilihan tidak valid!")