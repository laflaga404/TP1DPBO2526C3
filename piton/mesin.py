class Mesin:
    """
    Relasi: dimiliki oleh Kendaraan lewat KOMPOSISI (Kendaraan HAS-A Mesin).
    Mesin dibuat untuk satu kendaraan dan tidak berdiri sendiri.
    Atribut protected (underscore), akses lewat getter-setter agar tipe data terjaga.
    """

    def __init__(self, tipe: str = "", tenaga: int = 0, bahan_bakar: str = "", kapasitas: int = 0):
        self._tipe = str(tipe)
        self._tenaga = int(tenaga)              # HP
        self._bahan_bakar = str(bahan_bakar)
        self._kapasitas = int(kapasitas)        # kapasitas tangki (liter)

    # ---- Getter ----
    def get_tipe(self) -> str:
        return self._tipe

    def get_tenaga(self) -> int:
        return self._tenaga

    def get_bahan_bakar(self) -> str:
        return self._bahan_bakar

    def get_kapasitas(self) -> int:
        return self._kapasitas

    # ---- Setter ----
    def set_tipe(self, tipe: str) -> None:
        self._tipe = str(tipe)

    def set_tenaga(self, tenaga: int) -> None:
        self._tenaga = int(tenaga)

    def set_bahan_bakar(self, bahan_bakar: str) -> None:
        self._bahan_bakar = str(bahan_bakar)

    def set_kapasitas(self, kapasitas: int) -> None:
        self._kapasitas = int(kapasitas)

    def tampilkan_info(self):
        print("  [Mesin]")
        print(f"    Tipe          : {self._tipe}")
        print(f"    Tenaga        : {self._tenaga} HP")
        print(f"    Bahan Bakar   : {self._bahan_bakar}")
        print(f"    Kapasitas     : {self._kapasitas} liter")
