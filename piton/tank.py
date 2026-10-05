from kendaraan import Kendaraan


class Tank(Kendaraan):
    """INHERITANCE dari Kendaraan (hierarchical). Tambahan: armor, meriam, peluru."""

    def __init__(self, id_kendaraan: int = 0, nama: str = "", harga_sewa: int = 0,
                 mesin=None, status_sewa: str = "Tersedia",
                 ketebalan_armor: int = 0, jenis_meriam: str = "", kapasitas_peluru: int = 0):
        super().__init__(id_kendaraan, nama, harga_sewa, mesin, status_sewa)
        self._ketebalan_armor = int(ketebalan_armor)     # mm
        self._jenis_meriam = str(jenis_meriam)
        self._kapasitas_peluru = int(kapasitas_peluru)

    # ---- Getter ----
    def get_ketebalan_armor(self) -> int:
        return self._ketebalan_armor

    def get_jenis_meriam(self) -> str:
        return self._jenis_meriam

    def get_kapasitas_peluru(self) -> int:
        return self._kapasitas_peluru

    # ---- Setter ----
    def set_ketebalan_armor(self, ketebalan_armor: int) -> None:
        self._ketebalan_armor = int(ketebalan_armor)

    def set_jenis_meriam(self, jenis_meriam: str) -> None:
        self._jenis_meriam = str(jenis_meriam)

    def set_kapasitas_peluru(self, kapasitas_peluru: int) -> None:
        self._kapasitas_peluru = int(kapasitas_peluru)

    def get_jenis(self) -> str:
        return "Tank"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("  [Spesifik Tank]")
        print(f"    Ketebalan Armor : {self._ketebalan_armor} mm")
        print(f"    Jenis Meriam    : {self._jenis_meriam}")
        print(f"    Kapasitas Peluru: {self._kapasitas_peluru} butir")
