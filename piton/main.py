from mesin import Mesin
from tank import Tank
from apc import APC
from helikopter import Helikopter
from rental_kendaraan import RentalKendaraan


# ---------- Helper input ----------
# Hanya menerima bilangan bulat >= 0 (huruf, simbol, desimal, minus ditolak)
def input_integer(pesan: str) -> int:
    while True:
        s = input(pesan).strip()
        if not (s.isascii() and s.isdigit()):
            print("Input harus berupa angka (bilangan bulat 0 atau lebih)!")
        elif len(s) > 9:
            print("Angka terlalu besar!")
        else:
            return int(s)


# Kode kendaraan: harus angka >= 1 dan belum pernah dipakai. Diulang sampai valid.
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


# ---------- Tambah data ----------
def input_mesin() -> Mesin:
    print("-- Data Mesin --")
    tipe = input_string("Tipe Mesin         : ")
    tenaga = input_integer("Tenaga (HP)        : ")
    bahan_bakar = input_string("Bahan Bakar        : ")
    kapasitas = input_integer("Kapasitas Tangki(L): ")
    return Mesin(tipe, tenaga, bahan_bakar, kapasitas)


def tambah_data(rental: RentalKendaraan):
    print("\n******** TAMBAH KENDARAAN ********")
    print("1. Tank")
    print("2. APC")
    print("3. Helikopter")
    jenis = input_integer("Pilih jenis kendaraan: ")
    if jenis not in (1, 2, 3):
        print("Jenis tidak valid!")
        return

    id_k = input_kode_kendaraan(rental)

    nama = input_string("Nama               : ")
    harga = input_integer("Harga Sewa / hari  : ")
    st = 0
    while st not in (1, 2):
        st = input_integer("Status Sewa (1=Tersedia, 2=Disewa): ")
    status = "Tersedia" if st == 1 else "Disewa"
    mesin = input_mesin()

    # Tampilkan data SEBELUM ditambahkan
    print("\n######## DATA SEBELUM DITAMBAHKAN ########")
    rental.tampilkan_info()

    print("\n-- Data Spesifik --")
    if jenis == 1:
        armor = input_integer("Ketebalan Armor (mm): ")
        meriam = input_string("Jenis Meriam        : ")
        peluru = input_integer("Kapasitas Peluru    : ")
        rental.tambah_kendaraan(Tank(id_k, nama, harga, mesin, status, armor, meriam, peluru))
    elif jenis == 2:
        personel = input_integer("Kapasitas Personel : ")
        armor = input_string("Tipe Armor          : ")
        rental.tambah_kendaraan(APC(id_k, nama, harga, mesin, status, personel, armor))
    else:
        fungsi = input_string("Fungsi Helikopter   : ")
        angkut = input_integer("Kapasitas Angkut(kg): ")
        jarak = input_integer("Jarak Jangkauan (km): ")
        rental.tambah_kendaraan(Helikopter(id_k, nama, harga, mesin, status, fungsi, angkut, jarak))

    print("\nKendaraan berhasil ditambahkan!")

    # Tampilkan data SESUDAH ditambahkan
    print("\n######## DATA SESUDAH DITAMBAHKAN ########")
    rental.tampilkan_info()


# ---------- Menu ----------
def menu(rental: RentalKendaraan):
    while True:
        print("\n**************************************")
        print(f"  {rental.get_nama()}")
        print("**************************************")
        print("1. Tambah Kendaraan")
        print("2. Tampilkan Semua Data")
        print("3. Keluar")
        print("**************************************")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_data(rental)
        elif pilihan == "2":
            print("\n######## SEMUA DATA ########")
            rental.tampilkan_info()
        elif pilihan == "3":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak ada!")


def main():
    # Data awal
    rental = RentalKendaraan("Aska gunshop", "Bandung", "RN001", "022-1234567")

    rental.tambah_kendaraan(Tank(1, "Leopard 2A4", 15000000,
                                 Mesin("Diesel V12 Twin-Turbo", 1500, "Solar", 1200),
                                 "Tersedia", 700, "Rheinmetall 120mm", 42))

    rental.tambah_kendaraan(APC(2, "Anoa 6x6", 5000000,
                                Mesin("Diesel Turbo 6 Silinder", 320, "Solar", 300),
                                "Disewa", 10, "STANAG 4569 LV 1"))

    rental.tambah_kendaraan(Helikopter(3, "Bell 412", 12000000,
                                       Mesin("Turboshaft PT6T-3D", 1800, "Avtur", 800),
                                       "Tersedia", "Transport", 2000, 700))

    menu(rental)


if __name__ == "__main__":
    main()
