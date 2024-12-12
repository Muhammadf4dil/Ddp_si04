from animal import Animal

class Burung(Animal):
    def _init_(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        # Pemanggilan konstruktor parent class 
        super()._init_(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        # Pemanggilan method cetak dari parent class dan menambahkan detail burung
        super().cetak()
        print(f'Jenis bulu: {self.jenis_bulu}, Bunyi: {self.bunyi}')

# Membuat objek Burung
beo = Burung('Beo', 'Buah', 'Udara', 'Bertelur', 'Hijau', 'kamu jelek')
beo.cetak_burung()  # Memanggil method cetak_burung

# Membuat objek Burung Merpati
merpati = Burung('Merpati', 'Bijian', 'Udara', 'Bertelur', 'Putih', 'Coo')

# Memanggil method cetak_burung untuk menampilkan informasi merpati
merpati.cetak_burung()