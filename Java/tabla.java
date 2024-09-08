
import java.util.Scanner;
public class tabla {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduzca un numero: ");
        int numero = sc.nextInt();
        for (int i = 1; i <= 10; i++) {
            int resultado = numero *i;
            System.out.println(numero + "x" + i + " = " + resultado);
        }
    }
}