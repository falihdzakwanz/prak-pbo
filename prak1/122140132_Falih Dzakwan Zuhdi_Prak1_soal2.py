PI = 3.14
r = float(input("Masukkan jari-jari lingkaran: "))

if r < 0 :
    print("Jari-Jari tidak boleh negatif!")
else :
    luas = PI * r**2
    keliling = PI * 2 * r
    print("Luas lingkaran =", luas)
    print("Keliling lingkaran =", keliling)