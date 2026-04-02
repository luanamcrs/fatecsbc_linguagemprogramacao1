import java.util.*;

public class Exercicio {

    // FUNÇÃO MENU
    public static void exibirMenu() {
        System.out.println("\n1 - Adicionar");
        System.out.println("2 - Listar");
        System.out.println("3 - Sair");
    }

    // FUNÇÃO ESTOQUE
    public static String verificarEstoque(int qtd) {
        if (qtd < 5) {
            return "Estoque baixo!";
        } else {
            return "Estoque OK";
        }
    }

    // FUNÇÃO CABEÇALHO
    public static void exibirCabecalho() {
        System.out.println("=== SORVETERIA DO DENER ===");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<String> nomes = new ArrayList<>();
        ArrayList<Integer> quantidades = new ArrayList<>();
        ArrayList<Double> precos = new ArrayList<>();

        int op;

        do {
            exibirCabecalho();
            exibirMenu();

            op = sc.nextInt();

            if (op == 1) {
                System.out.print("Nome: ");
                String nome = sc.next();

                System.out.print("Quantidade: ");
                int qtd = sc.nextInt();

                System.out.print("Preço: ");
                double preco = sc.nextDouble();

                if (qtd < 0) {
                    System.out.println("Erro!");
                } else {
                    nomes.add(nome);
                    quantidades.add(qtd);
                    precos.add(preco);
                }
            }

            if (op == 2) {
                for (int i = 0; i < nomes.size(); i++) {
                    System.out.println("\nNome: " + nomes.get(i));
                    System.out.println("Quantidade: " + quantidades.get(i));
                    System.out.println("Preço: " + precos.get(i));
                    System.out.println("Status: " + verificarEstoque(quantidades.get(i)));
                }
            }

        } while (op != 3);

        sc.close();
    }
}