import java.util.ArrayList;

public class Exercicio {
    public static void exercicio(String[] args) {

        // ARRAY FIXO

        String[] nomesArray = {"Chocolate", "Morango", "Baunilha"};
        int[] qtdArray = {10, 3, 0};

        System.out.println("=== ARRAY FIXO ===");
        for (int i = 0; i < nomesArray.length; i++) {
            System.out.println(nomesArray[i] + " - " + qtdArray[i]);
        }

        // LISTA DINÂMICA

        ArrayList<String> nomes = new ArrayList<>();
        ArrayList<Integer> quantidades = new ArrayList<>();

        nomes.add("Chocolate");
        quantidades.add(10);

        nomes.add("Morango");
        quantidades.add(3);

        nomes.add("Baunilha");
        quantidades.add(0);

        System.out.println("\n=== LISTA DINÂMICA ===");

        for (int i = 0; i < nomes.size(); i++) {
            int qtd = quantidades.get(i);
            String status;

            if (qtd == 0) {
                status = "Em falta";
            } else if (qtd < 5) {
                status = "Alerta";
            } else {
                status = "OK";
            }

            System.out.println("Produto: " + nomes.get(i));
            System.out.println("Quantidade: " + qtd);
            System.out.println("Status: " + status);
            System.out.println("------------------");
        }
    }
}