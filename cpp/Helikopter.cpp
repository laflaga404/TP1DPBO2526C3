#pragma once
#include "Kendaraan.cpp"

class Helikopter : public Kendaraan {
private:
    string fungsiHelikopter;
    int kapasitasAngkut;   // kg
    int jarakJangkauan;    // km

public:
    // Constructor kosong
    Helikopter() {}

    // Constructor berparameter
    Helikopter(int idKendaraan, string nama, int hargaSewa, Mesin mesin, string statusSewa,
               string fungsiHelikopter, int kapasitasAngkut, int jarakJangkauan)
        : Kendaraan(idKendaraan, nama, hargaSewa, mesin, statusSewa) {
        this->fungsiHelikopter = fungsiHelikopter;
        this->kapasitasAngkut = kapasitasAngkut;
        this->jarakJangkauan = jarakJangkauan;
    }

    // ---- Getter ----
    string getFungsiHelikopter() { return fungsiHelikopter; }
    int getKapasitasAngkut() { return kapasitasAngkut; }
    int getJarakJangkauan() { return jarakJangkauan; }

    // ---- Setter ----
    void setFungsiHelikopter(string fungsiHelikopter) { this->fungsiHelikopter = fungsiHelikopter; }
    void setKapasitasAngkut(int kapasitasAngkut) { this->kapasitasAngkut = kapasitasAngkut; }
    void setJarakJangkauan(int jarakJangkauan) { this->jarakJangkauan = jarakJangkauan; }

    string getJenis() override { return "Helikopter"; }

    void tampilkanInfo() override {
        Kendaraan::tampilkanInfo();
        cout << "  [Spesifik Helikopter]" << endl;
        cout << "    Fungsi          : " << fungsiHelikopter << endl;
        cout << "    Kapasitas Angkut: " << kapasitasAngkut << " kg" << endl;
        cout << "    Jarak Jangkauan : " << jarakJangkauan << " km" << endl;
    }
};
