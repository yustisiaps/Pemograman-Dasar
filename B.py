class Mobil:
    def __init__(self, merek, warna, tahun):
        self.merek = merek
        self.warna = warna
        self.tahun = tahun

    def isi_bahan_bakar(self):
        print(f"Mobil {self.merek} sedang mengisi bahan bakar turbo.")

    def berhenti(self):
        print(f"Mobil {self.merek} berhenti.")

    def mengemudi(self):
        print(f"Mobil {self.merek} sedang melaju.")


# membuat objek dari kelas Mobil
mobil_saya = Mobil("Toyota", "Hitam", 2020)

# menggunakan objek mobil_saya
mobil_saya.isi_bahan_bakar()
mobil_saya.mengemudi()
mobil_saya.berhenti()
