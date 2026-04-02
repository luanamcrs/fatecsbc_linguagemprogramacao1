import java.util.*;

public class Exercicio {
    public static void exercicio(String[] args) {

        Scanner sc = new Scanner(System.in);

        // FOR

        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }

        // WHILE

        int num = 0;
        while (num <= 10) {
            System.out.print("Digite um número: ");
            num = sc.nextInt();
        }

        System.out.println("Obrigado!");

        // DO-WHILE

        int opcao;
        do {
            System.out.println("\n1 - Continuar");
            System.out.println("2 - Sair");
            opcao = sc.nextInt();
        } while (opcao != 2);

        // MÉDIA

        double soma = 0;
        for (int i = 0; i < 5; i++) {
            System.out.print("Nota: ");
            soma += sc.nextDouble();
        }

        System.out.println("Média: " + (soma / 5));

        // MVP FINAL

        ArrayList<String> produtos = new ArrayList<>();

        int op;
        do {
            System.out.println("\n1 - Adicionar");
            System.out.println("2 - Listar");
            System.out.println("3 - Sair");

            op = sc.nextInt();

            if (op == 1) {
                System.out.print("Nome: ");
                String nome = sc.next();

                System.out.print("Quantidade: ");
                int qtd = sc.nextInt();

                if (qtd < 0) {
                    System.out.println("Erro!");
                } else {
                    produtos.add(nome);
                }
            }

            if (op == 2) {
                for (String p : produtos) {
                    System.out.println(p);
                }
            }

        } while (op != 3);

        sc.close();
    }
}