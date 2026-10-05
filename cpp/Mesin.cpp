#pragma once
#include <iostream>
#include <string>
using namespace std;

class Mesin {
private:
    string tipe;
    int tenaga;        // dalam HP
    string bahanBakar;
    int kapasitas;     // kapasitas tangki (liter)

public:
    // Constructor kosong
    Mesin() {}

    // Constructor berparameter
    Mesin(string tipe, int tenaga, string bahanBakar, int kapasitas) {
        this->tipe = tipe;
        this->tenaga = tenaga;
        this->bahanBakar = bahanBakar;
        this->kapasitas = kapasitas;
    }

    // ---- Getter ----
    string getTipe() { return tipe; }
    int getTenaga() { return tenaga; }
    string getBahanBakar() { return bahanBakar; }
    int getKapasitas() { return kapasitas; }

    // ---- Setter ----
    void setTipe(string tipe) { this->tipe = tipe; }
    void setTenaga(int tenaga) { this->tenaga = tenaga; }
    void setBahanBakar(string bahanBakar) { this->bahanBakar = bahanBakar; }
    void setKapasitas(int kapasitas) { this->kapasitas = kapasitas; }

    void tampilkanInfo() {
        cout << "  [Mesin]" << endl;
        cout << "    Tipe          : " << tipe << endl;
        cout << "    Tenaga        : " << tenaga << " HP" << endl;
        cout << "    Bahan Bakar   : " << bahanBakar << endl;
        cout << "    Kapasitas     : " << kapasitas << " liter" << endl;
    }
};
