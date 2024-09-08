import java.util.Scanner;

public class Identificador_numeros {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean espar, espositivo;
        String Letra;

        System.out.println("Ingrese un número entero: ");
        int num = sc.nextInt();

        while (num != 0) {
            espar = num % 2 == 0 ? true : false;

            espositivo = num > 0 ? true : false;
            System.out.println(num + " es par " + espar + " y es" + espositivo);
            System.out.println("Cuadrado: " + num * num);
            System.out.println("Quieres continuar?");
            Letra = sc.next();
            if (Letra.equalsIgnoreCase("no")) {
                break;
            }
            System.out.println("Ingrese un número entero: ");
            num = sc.nextInt();
        }
    }
}