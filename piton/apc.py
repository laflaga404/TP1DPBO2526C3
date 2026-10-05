from kendaraan import Kendaraan


class APC(Kendaraan):
    """INHERITANCE dari Kendaraan (hierarchical). Tambahan: kapasitas personel, tipe armor."""

    def __init__(self, id_kendaraan: int = 0, nama: str = "", harga_sewa: int = 0,
                 mesin=None, status_sewa: str = "Tersedia",
                 kapasitas_personel: int = 0, tipe_armor: str = ""):
        super().__init__(id_kendaraan, nama, harga_sewa, mesin, status_sewa)
        self._kapasitas_personel = int(kapasitas_personel)
        self._tipe_armor = str(tipe_armor)

    # ---- Getter ----
    def get_kapasitas_personel(self) -> int:
        return self._kapasitas_personel

    def get_tipe_armor(self) -> str:
        return self._tipe_armor

    # ---- Setter ----
    def set_kapasitas_personel(self, kapasitas_personel: int) -> None:
        self._kapasitas_personel = int(kapasitas_personel)

    def set_tipe_armor(self, tipe_armor: str) -> None:
        self._tipe_armor = str(tipe_armor)

    def get_jenis(self) -> str:
        return "APC"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("  [Spesifik APC]")
        print(f"    Kapasitas Personel: {self._kapasitas_personel} orang")
        print(f"    Tipe Armor        : {self._tipe_armor}")
