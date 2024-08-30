#include <iostream>
using namespace std;

int hitung(int N) {
    if (N == 0 || N == 1) {
        return 1;
    }

    return N * hitung(N - 1);
}

int main() {
    int N;
    cout << "Masukkan N: ";
    cin >> N;

    int hasil = hitung(N);
        cout << "Faktorial dari " << N << " adalah " << hasil << endl;
    
    return 0;
}
