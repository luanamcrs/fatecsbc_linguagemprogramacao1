#include <iostream>
#include <vector>
using namespace std;

int main() {

    // ARRAY FIXO

    string nomesArray[3] = {"Chocolate", "Morango", "Baunilha"};
    int qtdArray[3] = {10, 3, 0};

    cout << "=== ARRAY FIXO ===" << endl;

    for (int i = 0; i < 3; i++) {
        cout << nomesArray[i] << " - " << qtdArray[i] << endl;
    }

    // LISTA DINÂMICA

    vector<string> nomes = {"Chocolate", "Morango", "Baunilha"};
    vector<int> quantidades = {10, 3, 0};

    cout << "\n=== LISTA DINÂMICA ===" << endl;

    for (int i = 0; i < nomes.size(); i++) {
        int qtd = quantidades[i];
        string status;

        if (qtd == 0) {
            status = "Em falta";
        } else if (qtd < 5) {
            status = "Alerta";
        } else {
            status = "OK";
        }

        cout << "Produto: " << nomes[i] << endl;
        cout << "Quantidade: " << qtd << endl;
        cout << "Status: " << status << endl;
        cout << "------------------" << endl;
    }

    return 0;
}