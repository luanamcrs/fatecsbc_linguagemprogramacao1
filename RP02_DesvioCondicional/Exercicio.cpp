#include <iostream>
using namespace std;

int main() {

    // PARTE 1 - Desvio Simples

    int quantidade = 3;

    if (quantidade < 5) {
        cout << "Atenção: Estoque baixo!" << endl;
    }

    // PARTE 2 - Desvio Composto

    quantidade = 7;

    if (quantidade < 5) {
        cout << "Atenção: Estoque baixo!" << endl;
    } else {
        cout << "Estoque OK!" << endl;
    }

    // PARTE 3 - Desvio Múltiplo

    quantidade = 2;

    if (quantidade < 1) {
        cout << "Em falta" << endl;
    } else if (quantidade < 5) {
        cout << "Alerta" << endl;
    } else {
        cout << "OK" << endl;
    }

    // SWITCH

    int codigo = 2;

    switch (codigo) {
        case 1:
            cout << "Disponível" << endl;
            break;
        case 2:
            cout << "Em Reposição" << endl;
            break;
        case 3:
            cout << "Descontinuado" << endl;
            break;
        default:
            cout << "Código inválido" << endl;
    }

    // TAREFA FINAL - VALIDAÇÃO

    string nome;
    float preco;

    cout << "\n=== Cadastro de Produto ===" << endl;

    cout << "Digite o nome do produto: ";
    cin >> nome;

    cout << "Digite a quantidade: ";
    cin >> quantidade;

    cout << "Digite o preço: ";
    cin >> preco;

    if (quantidade < 0) {
        cout << "Erro: A quantidade não pode ser negativa." << endl;
    } else {
        cout << "\nProduto cadastrado com sucesso!" << endl;
        cout << "Nome: " << nome << endl;
        cout << "Quantidade: " << quantidade << endl;
        cout << "Preço: " << preco << endl;
    }

    return 0;
}