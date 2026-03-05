#include <iostream>
using namespace std;

int main() {
    double valor1, valor2;
    int opcao;

    cout << "Digite o primeiro valor: ";
    cin >> valor1;

    cout << "Digite o segundo valor: ";
    cin >> valor2;

    cout << "\nEscolha a operacao:\n";
    cout << "1 - Soma\n";
    cout << "2 - Subtracao\n";
    cout << "3 - Multiplicacao\n";
    cout << "4 - Divisao\n";
    cout << "Opcao: ";
    cin >> opcao;

    if (opcao == 1) {
        cout << "Resultado: " << valor1 + valor2 << endl;
    }
    else if (opcao == 2) {
        cout << "Resultado: " << valor1 - valor2 << endl;
    }
    else if (opcao == 3) {
        cout << "Resultado: " << valor1 * valor2 << endl;
    }
    else if (opcao == 4) {
        if (valor2 != 0) {
            cout << "Resultado: " << valor1 / valor2 << endl;
        } else {
            cout << "Erro: divisao por zero!" << endl;
        }
    }
    else {
        cout << "Opcao invalida!" << endl;
    }

    return 0;
}