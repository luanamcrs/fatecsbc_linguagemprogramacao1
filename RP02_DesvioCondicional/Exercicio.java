import java.util.Scanner;

public class Exercicio {
    public static void main(String[] args) {

        // PARTE 1 - Desvio Simples

        int quantidade = 3;

        if (quantidade < 5) {
            System.out.println("Atenção: Estoque baixo!");
        }

        // PARTE 2 - Desvio Composto

        quantidade = 7;

        if (quantidade < 5) {
            System.out.println("Atenção: Estoque baixo!");
        } else {
            System.out.println("Estoque OK!");
        }

        // PARTE 3 - Desvio Múltiplo

        quantidade = 2;

        if (quantidade < 1) {
            System.out.println("Em falta");
        } else if (quantidade < 5) {
            System.out.println("Alerta");
        } else {
            System.out.println("OK");
        }

        // SWITCH

        int codigo = 2;

        switch (codigo) {
            case 1:
                System.out.println("Disponível");
                break;
            case 2:
                System.out.println("Em Reposição");
                break;
            case 3:
                System.out.println("Descontinuado");
                break;
            default:
                System.out.println("Código inválido");
        }

        // TAREFA FINAL - VALIDAÇÃO

        Scanner sc = new Scanner(System.in);

        System.out.println("\n=== Cadastro de Produto ===");

        System.out.print("Digite o nome do produto: ");
        String nome = sc.nextLine();

        System.out.print("Digite a quantidade: ");
        quantidade = sc.nextInt();

        System.out.print("Digite o preço: ");
        double preco = sc.nextDouble();

        if (quantidade < 0) {
            System.out.println("Erro: A quantidade não pode ser negativa.");
        } else {
            System.out.println("\nProduto cadastrado com sucesso!");
            System.out.println("Nome: " + nome);
            System.out.println("Quantidade: " + quantidade);
            System.out.println("Preço: " + preco);
        }

        sc.close();
    }
}