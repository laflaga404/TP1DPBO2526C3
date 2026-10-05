from kendaraan import Kendaraan


class Helikopter(Kendaraan):
    """INHERITANCE dari Kendaraan (hierarchical). Tambahan: fungsi, kapasitas angkut, jarak jangkauan."""

    def __init__(self, id_kendaraan: int = 0, nama: str = "", harga_sewa: int = 0,
                 mesin=None, status_sewa: str = "Tersedia",
                 fungsi_helikopter: str = "", kapasitas_angkut: int = 0, jarak_jangkauan: int = 0):
        super().__init__(id_kendaraan, nama, harga_sewa, mesin, status_sewa)
        self._fungsi_helikopter = str(fungsi_helikopter)
        self._kapasitas_angkut = int(kapasitas_angkut)   # kg
        self._jarak_jangkauan = int(jarak_jangkauan)     # km

    # ---- Getter ----
    def get_fungsi_helikopter(self) -> str:
        return self._fungsi_helikopter

    def get_kapasitas_angkut(self) -> int:
        return self._kapasitas_angkut

    def get_jarak_jangkauan(self) -> int:
        return self._jarak_jangkauan

    # ---- Setter ----
    def set_fungsi_helikopter(self, fungsi_helikopter: str) -> None:
        self._fungsi_helikopter = str(fungsi_helikopter)

    def set_kapasitas_angkut(self, kapasitas_angkut: int) -> None:
        self._kapasitas_angkut = int(kapasitas_angkut)

    def set_jarak_jangkauan(self, jarak_jangkauan: int) -> None:
        self._jarak_jangkauan = int(jarak_jangkauan)

    def get_jenis(self) -> str:
        return "Helikopter"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("  [Spesifikasi Helikopter]")
        print(f"    Fungsi          : {self._fungsi_helikopter}")
        print(f"    Kapasitas Angkut: {self._kapasitas_angkut} kg")
        print(f"    Jarak Jangkauan : {self._jarak_jangkauan} km")
