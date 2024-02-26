batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))
jumlah = 0

if batas_atas & batas_bawah < 0:
    print("Batas atas dan bawah tidak boleh di bawah nol!")
else:
    for i in range(batas_bawah, batas_atas + 1):
        if i % 2 == 1:
            print(i)
            jumlah += i
        
    print("Jumlah =", jumlah)