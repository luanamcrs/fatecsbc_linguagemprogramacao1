#include <iostream>
#include <vector>
using namespace std;

// FUNÇÃO MENU
void exibirMenu() {
    cout << "\n1 - Adicionar\n2 - Listar\n3 - Sair\n";
}

// FUNÇÃO ESTOQUE
string verificarEstoque(int qtd) {
    if (qtd < 5) {
        return "Estoque baixo!";
    } else {
        return "Estoque OK";
    }
}

// FUNÇÃO CABEÇALHO
void exibirCabecalho() {
    cout << "=== SORVETERIA DO DENER ===" << endl;
}

int main() {

    vector<string> nomes;
    vector<int> quantidades;
    vector<float> precos;

    int op;

    do {
        exibirCabecalho();
        exibirMenu();

        cin >> op;

        if (op == 1) {
            string nome;
            int qtd;
            float preco;

            cout << "Nome: ";
            cin >> nome;

            cout << "Quantidade: ";
            cin >> qtd;

            cout << "Preço: ";
            cin >> preco;

            if (qtd < 0) {
                cout << "Erro!" << endl;
            } else {
                nomes.push_back(nome);
                quantidades.push_back(qtd);
                precos.push_back(preco);
            }
        }

        if (op == 2) {
            for (int i = 0; i < nomes.size(); i++) {
                cout << "\nNome: " << nomes[i] << endl;
                cout << "Quantidade: " << quantidades[i] << endl;
                cout << "Preço: " << precos[i] << endl;
                cout << "Status: " << verificarEstoque(quantidades[i]) << endl;
            }
        }

    } while (op != 3);

    return 0;
}