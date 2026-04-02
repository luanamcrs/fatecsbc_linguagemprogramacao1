#include <iostream>
#include <vector>
using namespace std;

int main() {

    // FOR

    for (int i = 1; i <= 5; i++) {
        cout << i << endl;
    }

    // WHILE

    int num = 0;
    while (num <= 10) {
        cout << "Digite um número: ";
        cin >> num;
    }

    cout << "Obrigado!" << endl;

    // DO-WHILE

    int opcao;
    do {
        cout << "1-Continuar 2-Sair: ";
        cin >> opcao;
    } while (opcao != 2);

    // MVP FINAL
  
    vector<string> produtos;
    int op;

    do {
        cout << "\n1-Adicionar\n2-Listar\n3-Sair\n";
        cin >> op;

        if (op == 1) {
            string nome;
            int qtd;

            cout << "Nome: ";
            cin >> nome;

            cout << "Quantidade: ";
            cin >> qtd;

            if (qtd < 0) {
                cout << "Erro!" << endl;
            } else {
                produtos.push_back(nome);
            }
        }

        if (op == 2) {
            for (string p : produtos) {
                cout << p << endl;
            }
        }

    } while (op != 3);

    return 0;
}