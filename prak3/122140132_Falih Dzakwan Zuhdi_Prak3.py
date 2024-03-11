class Dagangan:
    jumlah_barang = 0
    list_barang = {}

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang[self.__nama] = {'stok': self.__stok, 'harga': self.__harga}

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        del Dagangan.list_barang[self.__nama]
        print(f"{self.__nama} dihapus dari toko!")

    @staticmethod
    def lihat_barang():
        print(f"Jumlah barang dagangan pada toko: {Dagangan.jumlah_barang} buah")
        i = 1
        for nama, detail in Dagangan.list_barang.items():
            print(f"{i}. {nama} seharga Rp {detail['harga']} (stok: {detail['stok']})")
            i+=1
        print()

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()
