from mesin import Mesin


class Kendaraan:
    """
    Superclass (Hierarchical Inheritance: Tank, APC, Helikopter).

    Relasi:
    - KOMPOSISI ke Mesin: objek Mesin menjadi bagian dari Kendaraan.
    - Dipakai sebagai superclass oleh Tank, APC, dan Helikopter.

    Atribut protected (underscore) supaya otomatis terwarisi ke subclass
    dan hanya diubah lewat getter-setter (tipe data selalu konsisten).
    """

    def __init__(self, id_kendaraan: int = 0, nama: str = "", harga_sewa: int = 0,
                 mesin: Mesin = None, status_sewa: str = "Tersedia"):
        self._id_kendaraan = int(id_kendaraan)   # angka saja: 1, 2, 3, ...
        self._nama = str(nama)
        self._harga_sewa = int(harga_sewa)               # per hari
        self._mesin = mesin if mesin is not None else Mesin()   # komposisi
        self._status_sewa = str(status_sewa)             # Tersedia / Disewa

    # ---- Getter ----
    def get_id_kendaraan(self) -> int:
        return self._id_kendaraan

    def get_nama(self) -> str:
        return self._nama

    def get_harga_sewa(self) -> int:
        return self._harga_sewa

    def get_mesin(self) -> Mesin:
        return self._mesin

    def get_status_sewa(self) -> str:
        return self._status_sewa

    # ---- Setter ----
    def set_id_kendaraan(self, id_kendaraan: int) -> None:
        self._id_kendaraan = int(id_kendaraan)

    def set_nama(self, nama: str) -> None:
        self._nama = str(nama)

    def set_harga_sewa(self, harga_sewa: int) -> None:
        self._harga_sewa = int(harga_sewa)

    def set_mesin(self, mesin: Mesin) -> None:
        self._mesin = mesin

    def set_status_sewa(self, status_sewa: str) -> None:
        self._status_sewa = str(status_sewa)

    # Polimorfisme: dioverride oleh subclass
    def get_jenis(self) -> str:
        return "Kendaraan"

    def tampilkan_info(self):
        print(f"  Jenis         : {self.get_jenis()}")
        print(f"  Kode Kendaraan: {self._id_kendaraan}")
        print(f"  Nama          : {self._nama}")
        print(f"  Harga Sewa    : Rp{self._harga_sewa} / hari")
        print(f"  Status Sewa   : {self._status_sewa}")
        self._mesin.tampilkan_info()
