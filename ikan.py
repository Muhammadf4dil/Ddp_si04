from animal import Animal

class Ikan(Animal):
    def _init_(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super()._init_(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f"Warna ikan: {self.warna_ikan} dan jenis ikan ini {self.jenis_ikan}")

# Membuat objek ikan nemo
nemo = Ikan('Nemo', 'Plankton', 'Air Laut', 'Bertelur', 'Oranye', 'Clownfish')
lele = Ikan('Lele', 'tai', 'Air Tawar', 'Bertelur', 'Hitam', 'Lele')

# Memanggil method cetak_ikan
nemo.cetak_ikan()
lele.cetak_ikan()