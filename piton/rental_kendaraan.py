class RentalKendaraan:
    """
    Relasi:
    - KOMPOSISI ke Kendaraan (daftar_kendaraan): kendaraan adalah bagian dari
      rental. Kalau objek rental dihapus, daftar kendaraannya ikut hilang.
    - daftar_kendaraan adalah ARRAY OF OBJECT (list berisi Tank/APC/Helikopter).
    """

    def __init__(self, nama: str = "", lokasi: str = "", id_rental: str = "",
                 kontak: str = "", daftar_kendaraan: list = None):
        self._nama = str(nama)
        self._lokasi = str(lokasi)
        self._id_rental = str(id_rental)
        self._kontak = str(kontak)
        self._daftar_kendaraan = list(daftar_kendaraan) if daftar_kendaraan else []

    # ---- Getter ----
    def get_nama(self) -> str:
        return self._nama

    def get_lokasi(self) -> str:
        return self._lokasi

    def get_id_rental(self) -> str:
        return self._id_rental

    def get_kontak(self) -> str:
        return self._kontak

    def get_daftar_kendaraan(self) -> list:
        return self._daftar_kendaraan

    # ---- Setter ----
    def set_nama(self, nama: str) -> None:
        self._nama = str(nama)

    def set_lokasi(self, lokasi: str) -> None:
        self._lokasi = str(lokasi)

    def set_id_rental(self, id_rental: str) -> None:
        self._id_rental = str(id_rental)

    def set_kontak(self, kontak: str) -> None:
        self._kontak = str(kontak)

    def set_daftar_kendaraan(self, daftar_kendaraan: list) -> None:
        self._daftar_kendaraan = list(daftar_kendaraan)

    def tambah_kendaraan(self, kendaraan) -> None:
        self._daftar_kendaraan.append(kendaraan)

    def cari_by_id(self, id_kendaraan: int):
        for k in self._daftar_kendaraan:
            if k.get_id_kendaraan() == id_kendaraan:
                return k
        return None

    def tampilkan_info(self):
        print("=" * 50)
        print(f"ID Rental       : {self._id_rental}")
        print(f"Nama            : {self._nama}")
        print(f"Lokasi          : {self._lokasi}")
        print(f"Kontak          : {self._kontak}")
        print(f"Jumlah Kendaraan: {len(self._daftar_kendaraan)}")
        print("=" * 50)

        if not self._daftar_kendaraan:
            print("Belum ada kendaraan.")
            return

        for no, k in enumerate(self._daftar_kendaraan, start=1):
            print(f"\n--- Kendaraan #{no} ---")
            k.tampilkan_info()   # polimorfisme
