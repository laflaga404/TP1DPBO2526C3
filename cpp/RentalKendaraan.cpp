#pragma once
#include <iostream>
#include <string>
#include <vector>
#include "Kendaraan.cpp"
using namespace std;

// Composition: RentalKendaraan HAS-A daftar Kendaraan.
// Rental yang membuat/memiliki objek kendaraan, jadi saat Rental dihancurkan
// semua Kendaraan di dalamnya ikut dihapus (lihat destructor).
class RentalKendaraan {
private:
    string nama;
    string lokasi;
    string idRental;
    string kontak;
    vector<Kendaraan*> daftarKendaraan;   // ARRAY OF OBJECT (pointer, supaya polimorfik)

public:
    // Constructor kosong
    RentalKendaraan() {}

    // Constructor berparameter
    RentalKendaraan(string nama, string lokasi, string idRental, string kontak) {
        this->nama = nama;
        this->lokasi = lokasi;
        this->idRental = idRental;
        this->kontak = kontak;
    }

    // Rental pemilik tunggal -> larang copy agar tidak terjadi double delete
    RentalKendaraan(const RentalKendaraan&) = delete;
    RentalKendaraan& operator=(const RentalKendaraan&) = delete;

    // Destructor: hapus semua kendaraan (sifat composition)
    ~RentalKendaraan() {
        for (auto k : daftarKendaraan) delete k;
        daftarKendaraan.clear();
    }

    // ---- Getter ----
    string getNama() { return nama; }
    string getLokasi() { return lokasi; }
    string getIdRental() { return idRental; }
    string getKontak() { return kontak; }
    vector<Kendaraan*>& getDaftarKendaraan() { return daftarKendaraan; }

    // ---- Setter ----
    void setNama(string nama) { this->nama = nama; }
    void setLokasi(string lokasi) { this->lokasi = lokasi; }
    void setIdRental(string idRental) { this->idRental = idRental; }
    void setKontak(string kontak) { this->kontak = kontak; }

    // Rental mengambil alih kepemilikan pointer
    void tambahKendaraan(Kendaraan* k) { daftarKendaraan.push_back(k); }

    Kendaraan* cariById(int id) {
        for (auto k : daftarKendaraan) {
            if (k->getIdKendaraan() == id) return k;
        }
        return nullptr;
    }

    void tampilkanInfo() {
        cout << "==================================================" << endl;
        cout << "ID Rental   : " << idRental << endl;
        cout << "Nama        : " << nama << endl;
        cout << "Lokasi      : " << lokasi << endl;
        cout << "Kontak      : " << kontak << endl;
        cout << "Jumlah Kendaraan: " << daftarKendaraan.size() << endl;
        cout << "==================================================" << endl;

        if (daftarKendaraan.empty()) {
            cout << "Belum ada kendaraan." << endl;
            return;
        }

        int no = 1;
        for (auto k : daftarKendaraan) {
            cout << "\n--- Kendaraan #" << no++ << " ---" << endl;
            k->tampilkanInfo();   // polimorfisme
        }
    }
};
