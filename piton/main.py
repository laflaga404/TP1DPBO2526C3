from mesin import Mesin
from tank import Tank
from apc import APC
from helikopter import Helikopter
from rental_kendaraan import RentalKendaraan


# ---------- Helper input ----------
def input_integer(pesan: str) -> int:
    while True:
        s = input(pesan).strip()

        # Izinkan angka dengan titik/koma sebagai pemisah ribuan.
        s_bersih = s.replace('.', '').replace(',', '')

        if not s_bersih.isascii() or not s_bersih.isdigit():
            print("Input harus berupa angka bulat 0 atau lebih!")
            continue

        return int(s_bersih)


def input_kode_kendaraan(rental: RentalKendaraan) -> int:
    while True:
        id_k = input_integer("Kode Kendaraan (angka): ")

        if id_k < 1:
            print("Kode harus angka 1 atau lebih!")
        elif rental.cari_by_id(id_k) is not None:
            print(f"Kode {id_k} sudah dipakai, coba kode lain!")
        else:
            return id_k


def input_string(pesan: str) -> str:
    while True:
        s = input(pesan).strip()
        if s:
            return s
        print("Input tidak boleh kosong!")


# ---------- Input Mesin ----------
def input_mesin() -> Mesin:
    print("\n-- Data Mesin --")
    tipe = input_string("Tipe Mesin          : ")
    tenaga = input_integer("Tenaga (HP)         : ")
    bahan_bakar = input_string("Bahan Bakar         : ")
    kapasitas = input_integer("Kapasitas Tangki (L): ")

    return Mesin(tipe, tenaga, bahan_bakar, kapasitas)


# ---------- Tambah Data ----------
def tambah_data(rental: RentalKendaraan):
    print("\n" + "=" * 45)
    print("           TAMBAH KENDARAAN")
    print("=" * 45)
    print("1. Tank")
    print("2. APC")
    print("3. Helikopter")
    print("=" * 45)

    while True:
        jenis = input_integer("Pilih jenis kendaraan: ")
        if jenis in (1, 2, 3):
            break
        print("Pilihan tidak valid! Pilih 1, 2, atau 3.")

    id_k = input_kode_kendaraan(rental)
    nama = input_string("Nama                : ")
    harga = input_integer("Harga Sewa / hari   : ")

    while True:
        st = input_integer("Status Sewa (1=Tersedia, 2=Disewa): ")
        if st in (1, 2):
            break
        print("Status tidak valid! Pilih 1 atau 2.")

    status = "Tersedia" if st == 1 else "Disewa"
    mesin = input_mesin()

    # Data spesifik tiap jenis kendaraan.
    print("\n-- Data Spesifik --")

    if jenis == 1:
        armor = input_integer("Ketebalan Armor (mm): ")
        meriam = input_string("Jenis Meriam         : ")
        peluru = input_integer("Kapasitas Peluru     : ")

        kendaraan = Tank(
            id_k, nama, harga, mesin, status,
            armor, meriam, peluru
        )

    elif jenis == 2:
        personel = input_integer("Kapasitas Personel  : ")
        armor = input_string("Tipe Armor           : ")

        kendaraan = APC(
            id_k, nama, harga, mesin, status,
            personel, armor
        )

    else:
        fungsi = input_string("Fungsi Helikopter    : ")
        angkut = input_integer("Kapasitas Angkut (kg): ")
        jarak = input_integer("Jarak Jangkauan (km) : ")

        kendaraan = Helikopter(
            id_k, nama, harga, mesin, status,
            fungsi, angkut, jarak
        )

    rental.tambah_kendaraan(kendaraan)

    print("\n" + "=" * 45)
    print("      KENDARAAN BERHASIL DITAMBAHKAN")
    print("=" * 45)
    print(f"Kode Kendaraan : {id_k}")
    print(f"Nama           : {nama}")
    print(f"Jenis          : {kendaraan.get_jenis()}")
    print(f"Status         : {status}")
    print(f"Total Kendaraan: {len(rental.get_daftar_kendaraan())}")
    print("=" * 45)


def tampilkan_semua(rental: RentalKendaraan):
    print("\n" + "=" * 50)
    print("              DATA KENDARAAN")
    print("=" * 50)
    rental.tampilkan_info()
    print("=" * 50)


# ---------- Menu ----------
def menu(rental: RentalKendaraan):
    while True:
        print("\n" + "=" * 45)
        print(f"           {rental.get_nama()}")
        print("=" * 45)
        print("1. Tambah Kendaraan")
        print("2. Tampilkan Semua Data")
        print("3. Keluar")
        print("=" * 45)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_data(rental)
        elif pilihan == "2":
            tampilkan_semua(rental)
        elif pilihan == "3":
            print("\nProgram selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak ada! Silakan pilih 1, 2, atau 3.")


def main():
    rental = RentalKendaraan(
        "Aska gunshop",
        "Bandung",
        "RN001",
        "022-1234567"
    )

    # Data awal
    rental.tambah_kendaraan(
        Tank(
            1,
            "Leopard 2A4",
            15000000,
            Mesin("Diesel V12 Twin-Turbo", 1500, "Solar", 1200),
            "Tersedia",
            700,
            "Rheinmetall 120mm",
            42
        )
    )

    rental.tambah_kendaraan(
        APC(
            2,
            "Anoa 6x6",
            5000000,
            Mesin("Diesel Turbo 6 Silinder", 320, "Solar", 300),
            "Disewa",
            10,
            "STANAG 4569 LV 1"
        )
    )

    rental.tambah_kendaraan(
        Helikopter(
            3,
            "Bell 412",
            12000000,
            Mesin("Turboshaft PT6T-3D", 1800, "Avtur", 800),
            "Tersedia",
            "Transport",
            2000,
            700
        )
    )

    menu(rental)


if __name__ == "__main__":
    main()
from mesin import Mesin
from tank import Tank
from apc import APC
from helikopter import Helikopter
from rental_kendaraan import RentalKendaraan


# ---------- Helper input ----------
def input_integer(pesan: str) -> int:
    while True:
        s = input(pesan).strip()

        # Izinkan angka dengan titik/koma sebagai pemisah ribuan.
        s_bersih = s.replace('.', '').replace(',', '')

        if not s_bersih.isascii() or not s_bersih.isdigit():
            print("Input harus berupa angka bulat 0 atau lebih!")
            continue

        return int(s_bersih)


def input_kode_kendaraan(rental: RentalKendaraan) -> int:
    while True:
        id_k = input_integer("Kode Kendaraan (angka): ")

        if id_k < 1:
            print("Kode harus angka 1 atau lebih!")
        elif rental.cari_by_id(id_k) is not None:
            print(f"Kode {id_k} sudah dipakai, coba kode lain!")
        else:
            return id_k


def input_string(pesan: str) -> str:
    while True:
        s = input(pesan).strip()
        if s:
            return s
        print("Input tidak boleh kosong!")


# ---------- Input Mesin ----------
def input_mesin() -> Mesin:
    print("\n-- Data Mesin --")
    tipe = input_string("Tipe Mesin          : ")
    tenaga = input_integer("Tenaga (HP)         : ")
    bahan_bakar = input_string("Bahan Bakar         : ")
    kapasitas = input_integer("Kapasitas Tangki (L): ")

    return Mesin(tipe, tenaga, bahan_bakar, kapasitas)


# ---------- Tambah Data ----------
def tambah_data(rental: RentalKendaraan):
    print("\n" + "=" * 45)
    print("           TAMBAH KENDARAAN")
    print("=" * 45)
    print("1. Tank")
    print("2. APC")
    print("3. Helikopter")
    print("=" * 45)

    while True:
        jenis = input_integer("Pilih jenis kendaraan: ")
        if jenis in (1, 2, 3):
            break
        print("Pilihan tidak valid! Pilih 1, 2, atau 3.")

    id_k = input_kode_kendaraan(rental)
    nama = input_string("Nama                : ")
    harga = input_integer("Harga Sewa / hari   : ")

    while True:
        st = input_integer("Status Sewa (1=Tersedia, 2=Disewa): ")
        if st in (1, 2):
            break
        print("Status tidak valid! Pilih 1 atau 2.")

    status = "Tersedia" if st == 1 else "Disewa"
    mesin = input_mesin()

    # Data spesifik tiap jenis kendaraan.
    print("\n-- Data Spesifik --")

    if jenis == 1:
        armor = input_integer("Ketebalan Armor (mm): ")
        meriam = input_string("Jenis Meriam         : ")
        peluru = input_integer("Kapasitas Peluru     : ")

        kendaraan = Tank(
            id_k, nama, harga, mesin, status,
            armor, meriam, peluru
        )

    elif jenis == 2:
        personel = input_integer("Kapasitas Personel  : ")
        armor = input_string("Tipe Armor           : ")

        kendaraan = APC(
            id_k, nama, harga, mesin, status,
            personel, armor
        )

    else:
        fungsi = input_string("Fungsi Helikopter    : ")
        angkut = input_integer("Kapasitas Angkut (kg): ")
        jarak = input_integer("Jarak Jangkauan (km) : ")

        kendaraan = Helikopter(
            id_k, nama, harga, mesin, status,
            fungsi, angkut, jarak
        )

    rental.tambah_kendaraan(kendaraan)

    print("\n" + "=" * 45)
    print("      KENDARAAN BERHASIL DITAMBAHKAN")
    print("=" * 45)
    print(f"Kode Kendaraan : {id_k}")
    print(f"Nama           : {nama}")
    print(f"Jenis          : {kendaraan.get_jenis()}")
    print(f"Status         : {status}")
    print(f"Total Kendaraan: {len(rental.get_daftar_kendaraan())}")
    print("=" * 45)


def tampilkan_semua(rental: RentalKendaraan):
    print("\n" + "=" * 50)
    print("              DATA KENDARAAN")
    print("=" * 50)
    rental.tampilkan_info()
    print("=" * 50)


# ---------- Menu ----------
def menu(rental: RentalKendaraan):
    while True:
        print("\n" + "=" * 45)
        print(f"           {rental.get_nama()}")
        print("=" * 45)
        print("1. Tambah Kendaraan")
        print("2. Tampilkan Semua Data")
        print("3. Keluar")
        print("=" * 45)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_data(rental)
        elif pilihan == "2":
            tampilkan_semua(rental)
        elif pilihan == "3":
            print("\nProgram selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak ada! Silakan pilih 1, 2, atau 3.")


def main():
    rental = RentalKendaraan(
        "Aska gunshop",
        "Bandung",
        "RN001",
        "022-1234567"
    )

    # Data awal
    rental.tambah_kendaraan(
        Tank(
            1,
            "Leopard 2A4",
            15000000,
            Mesin("Diesel V12 Twin-Turbo", 1500, "Solar", 1200),
            "Tersedia",
            700,
            "Rheinmetall 120mm",
            42
        )
    )

    rental.tambah_kendaraan(
        APC(
            2,
            "Anoa 6x6",
            5000000,
            Mesin("Diesel Turbo 6 Silinder", 320, "Solar", 300),
            "Disewa",
            10,
            "STANAG 4569 LV 1"
        )
    )

    rental.tambah_kendaraan(
        Helikopter(
            3,
            "Bell 412",
            12000000,
            Mesin("Turboshaft PT6T-3D", 1800, "Avtur", 800),
            "Tersedia",
            "Transport",
            2000,
            700
        )
    )

    menu(rental)


if __name__ == "__main__":
    main()
