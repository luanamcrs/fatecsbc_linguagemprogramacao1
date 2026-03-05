import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        double valor1, valor2;
        int opcao;

        System.out.print("Digite o primeiro valor: ");
        valor1 = entrada.nextDouble();

        System.out.print("Digite o segundo valor: ");
        valor2 = entrada.nextDouble();

        System.out.println("\nEscolha a operação:");
        System.out.println("1 - Soma");
        System.out.println("2 - Subtração");
        System.out.println("3 - Multiplicação");
        System.out.println("4 - Divisão");

        System.out.print("Opção: ");
        opcao = entrada.nextInt();

        switch (opcao) {

            case 1:
                System.out.println("Resultado: " + (valor1 + valor2));
                break;

            case 2:
                System.out.println("Resultado: " + (valor1 - valor2));
                break;

            case 3:
                System.out.println("Resultado: " + (valor1 * valor2));
                break;

            case 4:
                if (valor2 != 0) {
                    System.out.println("Resultado: " + (valor1 / valor2));
                } else {
                    System.out.println("Erro: divisão por zero!");
                }
                break;

            default:
                System.out.println("Opção inválida!");
        }

        entrada.close();
    }
}