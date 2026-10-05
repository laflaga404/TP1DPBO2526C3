#pragma once
#include <iostream>
#include <string>
#include "Mesin.cpp"
using namespace std;

// Superclass (Hierarchical Inheritance: Tank, APC, Helikopter)
// Composition: Kendaraan HAS-A Mesin (objek Mesin menempel di dalam Kendaraan)
class Kendaraan {
protected:
    int idKendaraan;     // angka saja: 1, 2, 3, ...
    string nama;
    int hargaSewa;       // per hari
    Mesin mesin;         // COMPOSITION
    string statusSewa;   // "Tersedia" / "Disewa"

public:
    // Constructor kosong
    Kendaraan() {}

    // Constructor berparameter
    Kendaraan(int idKendaraan, string nama, int hargaSewa, Mesin mesin, string statusSewa) {
        this->idKendaraan = idKendaraan;
        this->nama = nama;
        this->hargaSewa = hargaSewa;
        this->mesin = mesin;
        this->statusSewa = statusSewa;
    }

    // Destructor virtual: wajib agar delete lewat pointer Kendaraan* aman
    virtual ~Kendaraan() {}

    // ---- Getter ----
    int getIdKendaraan() { return idKendaraan; }
    string getNama() { return nama; }
    int getHargaSewa() { return hargaSewa; }
    Mesin& getMesin() { return mesin; }
    string getStatusSewa() { return statusSewa; }

    // ---- Setter ----
    void setIdKendaraan(int idKendaraan) { this->idKendaraan = idKendaraan; }
    void setNama(string nama) { this->nama = nama; }
    void setHargaSewa(int hargaSewa) { this->hargaSewa = hargaSewa; }
    void setMesin(Mesin mesin) { this->mesin = mesin; }
    void setStatusSewa(string statusSewa) { this->statusSewa = statusSewa; }

    // Polimorfisme: dioverride oleh subclass
    virtual string getJenis() { return "Kendaraan"; }

    virtual void tampilkanInfo() {
        cout << "  Jenis         : " << getJenis() << endl;
        cout << "  Kode Kendaraan: " << idKendaraan << endl;
        cout << "  Nama          : " << nama << endl;
        cout << "  Harga Sewa    : Rp" << hargaSewa << " / hari" << endl;
        cout << "  Status Sewa   : " << statusSewa << endl;
        mesin.tampilkanInfo();
    }
};
