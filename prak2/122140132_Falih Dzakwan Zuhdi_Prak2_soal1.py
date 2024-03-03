class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=False):
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__isMahasiswa = isMahasiswa

    def set_nama(self, new_nama):
        self.__nama = new_nama

    def set_nim(self, new_nim):
        self.__nim = new_nim

    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def perkenalan_diri(self):
        return f"Perkenalkan nama saya {self.__nama} dengan nim {self.__nim} dari angakatan {self.__angkatan}"

    def donatur_kampus(self):
        if self.__isMahasiswa == True:
            if self.__angkatan < 2015:
                return "Sungkem donatur kampus"
            else:
                return "Bukan donatur kampus"
        else :
            return "Bukan mahasiswa"
    def hitung_jumlah_huruf(self):
        return len(self.__nama)

mahasiswa1 = Mahasiswa(nim="12345", nama="Brian", angkatan=2018)
mahasiswa2 = Mahasiswa(nim="12346", nama="May", angkatan=2014, isMahasiswa=True)

print(f"Mahasiswa 1: Nama = {mahasiswa1.get_nama()}, NIM = {mahasiswa1.get_nim()}")
print(f"Mahasiswa 2: Nama = {mahasiswa2.get_nama()}, NIM = {mahasiswa2.get_nim()}")
print(f"Perkenalan Mahasiswa 1 : {mahasiswa1.perkenalan_diri()}")
print(f"Perkenalan Mahasiswa 2 : {mahasiswa2.perkenalan_diri()}")
print(f"Apakah Mahasiswa 1 donatur kampus ? : {mahasiswa1.donatur_kampus()}")
print(f"Apakah Mahasiswa 2 donatur kampus ? : {mahasiswa2.donatur_kampus()}")
print(f"Jumlah huruf nama Mahasiswa 1: {mahasiswa1.hitung_jumlah_huruf()}")
print(f"Jumlah huruf nama Mahasiswa 2: {mahasiswa2.hitung_jumlah_huruf()}")

mahasiswa1.set_nama("Freddy")
mahasiswa1.set_nim("654321")

print(f"Mahasiswa 1: Nama = {mahasiswa1.get_nama()}, NIM = {mahasiswa1.get_nim()}")
