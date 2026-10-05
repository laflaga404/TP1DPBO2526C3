#pragma once
#include "Kendaraan.cpp"

class APC : public Kendaraan {
private:
    int kapasitasPersonel;
    string tipeArmor;

public:
    // Constructor kosong
    APC()  {}

    // Constructor berparameter
    APC(int idKendaraan, string nama, int hargaSewa, Mesin mesin, string statusSewa,
        int kapasitasPersonel, string tipeArmor)
        : Kendaraan(idKendaraan, nama, hargaSewa, mesin, statusSewa) {
        this->kapasitasPersonel = kapasitasPersonel;
        this->tipeArmor = tipeArmor;
    }

    // ---- Getter ----
    int getKapasitasPersonel() { return kapasitasPersonel; }
    string getTipeArmor() { return tipeArmor; }

    // ---- Setter ----
    void setKapasitasPersonel(int kapasitasPersonel) { this->kapasitasPersonel = kapasitasPersonel; }
    void setTipeArmor(string tipeArmor) { this->tipeArmor = tipeArmor; }

    string getJenis() override { return "APC"; }

    void tampilkanInfo() override {
        Kendaraan::tampilkanInfo();
        cout << "  [Spesifik APC]" << endl;
        cout << "    Kapasitas Personel: " << kapasitasPersonel << " orang" << endl;
        cout << "    Tipe Armor        : " << tipeArmor << endl;
    }
};
