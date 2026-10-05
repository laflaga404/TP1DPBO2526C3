#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include "Mesin.cpp"
#include "Kendaraan.cpp"
#include "Tank.cpp"
#include "APC.cpp"
#include "Helikopter.cpp"
#include "RentalKendaraan.cpp"

using namespace std;

// ---------- Helper input ----------
// Hanya menerima bilangan bulat >= 0 (huruf, simbol, spasi di tengah, desimal ditolak)
int inputInteger(string pesan) {
    string s;
    while (true) {
        cout << pesan;
        getline(cin, s);

        // buang spasi di awal & akhir
        size_t awal = s.find_first_not_of(" \t");
        size_t akhir = s.find_last_not_of(" \t");
        s = (awal == string::npos) ? "" : s.substr(awal, akhir - awal + 1);

        bool semuaAngka = !s.empty() && all_of(s.begin(), s.end(),
            [](unsigned char c) { return isdigit(c); });

        if (!semuaAngka) {
            cout << "Input harus berupa angka (bilangan bulat 0 atau lebih)!" << endl;
        } else if (s.length() > 9) {
            cout << "Angka terlalu besar!" << endl;
        } else {
            return stoi(s);
        }
    }
}

// Kode kendaraan: harus angka >= 1 dan belum pernah dipakai. Diulang sampai valid.
int inputKodeKendaraan(RentalKendaraan &rental) {
    while (true) {
        int id = inputInteger("Kode Kendaraan (angka): ");
        if (id < 1) {
            cout << "Kode harus angka 1 atau lebih!" << endl;
        } else if (rental.cariById(id) != nullptr) {
            cout << "Kode " << id << " sudah dipakai, coba kode lain!" << endl;
        } else {
            return id;
        }
    }
}

string inputString(string pesan) {
    string s;
    while (true) {
        cout << pesan;
        getline(cin, s);
        if (!s.empty()) return s;
        cout << "Input tidak boleh kosong!" << endl;
    }
}

// ---------- Tambah data ----------
Mesin inputMesin() {
    cout << "-- Data Mesin --" << endl;
    string tipe = inputString("Tipe Mesin         : ");
    int tenaga = inputInteger("Tenaga (HP)        : ");
    string bahanBakar = inputString("Bahan Bakar        : ");
    int kapasitas = inputInteger("Kapasitas Tangki(L): ");
    return Mesin(tipe, tenaga, bahanBakar, kapasitas);
}

void tambahData(RentalKendaraan &rental) {
    cout << "\n=============================================" << endl;
    cout << "           TAMBAH KENDARAAN" << endl;
    cout << "=============================================" << endl;
    cout << "1. Tank" << endl;
    cout << "2. APC" << endl;
    cout << "3. Helikopter" << endl;
    cout << "=============================================" << endl;
    int jenis = inputInteger("Pilih jenis kendaraan: ");
    if (jenis < 1 || jenis > 3) {
        cout << "Jenis tidak valid!" << endl;
        return;
    }

    int id = inputKodeKendaraan(rental);

    string nama = inputString("Nama                : ");
    int harga = inputInteger("Harga Sewa / hari   : ");
    int st = 0;
    while (st != 1 && st != 2) st = inputInteger("Status Sewa (1=Tersedia, 2=Disewa): ");
    string status = (st == 1) ? "Tersedia" : "Disewa";
    Mesin mesin = inputMesin();

    cout << "\n-- Data Spesifik --" << endl;
    if (jenis == 1) {
        int armor = inputInteger("Ketebalan Armor (mm): ");
        string meriam = inputString("Jenis Meriam         : ");
        int peluru = inputInteger("Kapasitas Peluru     : ");
        rental.tambahKendaraan(new Tank(id, nama, harga, mesin, status, armor, meriam, peluru));
    } else if (jenis == 2) {
        int personel = inputInteger("Kapasitas Personel : ");
        string armor = inputString("Tipe Armor          : ");
        rental.tambahKendaraan(new APC(id, nama, harga, mesin, status, personel, armor));
    } else {
        string fungsi = inputString("Fungsi Helikopter   : ");
        int angkut = inputInteger("Kapasitas Angkut(kg): ");
        int jarak = inputInteger("Jarak Jangkauan (km): ");
        rental.tambahKendaraan(new Helikopter(id, nama, harga, mesin, status, fungsi, angkut, jarak));
    }

    cout << "\n=============================================" << endl;
    cout << "      KENDARAAN BERHASIL DITAMBAHKAN" << endl;
    cout << "=============================================" << endl;
    cout << "Kode Kendaraan : " << id << endl;
    cout << "Nama           : " << nama << endl;
    cout << "Jenis          : " << (jenis == 1 ? "Tank" : (jenis == 2 ? "APC" : "Helikopter")) << endl;
    cout << "Status         : " << status << endl;
    cout << "=============================================" << endl;
}

// ---------- Menu ----------
void menu(RentalKendaraan &rental) {
    while (true) {
        cout << "\n=============================================" << endl;
        cout << "           " << rental.getNama() << endl;
        cout << "=============================================" << endl;
        cout << "1. Tambah Kendaraan" << endl;
        cout << "2. Tampilkan Semua Data" << endl;
        cout << "3. Keluar" << endl;
        cout << "=============================================" << endl;
        cout << "Pilih menu: ";
        string pilihan;
        getline(cin, pilihan);

        if (pilihan == "1") {
            tambahData(rental);
        } else if (pilihan == "2") {
            cout << "\n==================================================" << endl;
            cout << "              DATA KENDARAAN" << endl;
            cout << "==================================================" << endl;
            rental.tampilkanInfo();
        } else if (pilihan == "3") {
            cout << "Sampai jumpa!" << endl;
            break;
        } else {
            cout << "Pilihan tidak ada!" << endl;
        }
    }
}

int main() {
    // Data awal (constructor berparameter)
    RentalKendaraan rental("Aska gunshop", "Bandung", "RN001", "022-1234567");

    rental.tambahKendaraan(new Tank(1, "Leopard 2A4", 15000000,
        Mesin("Diesel V12 Twin-Turbo", 1500, "Solar", 1200),
        "Tersedia", 700, "Rheinmetall 120mm", 42));

    rental.tambahKendaraan(new APC(2, "Anoa 6x6", 5000000,
        Mesin("Diesel Turbo 6 Silinder", 320, "Solar", 300),
        "Disewa", 10, "STANAG 4569 LV 1"));

    rental.tambahKendaraan(new Helikopter(3, "Bell 412", 12000000,
        Mesin("Turboshaft PT6T-3D", 1800, "Avtur", 800),
        "Tersedia", "Transport", 2000, 700));

    menu(rental);
    return 0;
}
