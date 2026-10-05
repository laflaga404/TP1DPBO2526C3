#pragma once
#include "Kendaraan.cpp"

class Tank : public Kendaraan {
private:
    int ketebalanArmor;   // mm
    string jenisMeriam;
    int kapasitasPeluru;

public:
    // Constructor kosong
    Tank()  {}

    // Constructor berparameter
    Tank(int idKendaraan, string nama, int hargaSewa, Mesin mesin, string statusSewa,
         int ketebalanArmor, string jenisMeriam, int kapasitasPeluru)
        : Kendaraan(idKendaraan, nama, hargaSewa, mesin, statusSewa) {
        this->ketebalanArmor = ketebalanArmor;
        this->jenisMeriam = jenisMeriam;
        this->kapasitasPeluru = kapasitasPeluru;
    }

    // ---- Getter ----
    int getKetebalanArmor() { return ketebalanArmor; }
    string getJenisMeriam() { return jenisMeriam; }
    int getKapasitasPeluru() { return kapasitasPeluru; }

    // ---- Setter ----
    void setKetebalanArmor(int ketebalanArmor) { this->ketebalanArmor = ketebalanArmor; }
    void setJenisMeriam(string jenisMeriam) { this->jenisMeriam = jenisMeriam; }
    void setKapasitasPeluru(int kapasitasPeluru) { this->kapasitasPeluru = kapasitasPeluru; }

    string getJenis() override { return "Tank"; }

    void tampilkanInfo() override {
        Kendaraan::tampilkanInfo();
        cout << "  [Spesifik Tank]" << endl;
        cout << "    Ketebalan Armor : " << ketebalanArmor << " mm" << endl;
        cout << "    Jenis Meriam    : " << jenisMeriam << endl;
        cout << "    Kapasitas Peluru: " << kapasitasPeluru << " butir" << endl;
    }
};
