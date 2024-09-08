
import java.util.Random;
import java.util.Scanner;
public class Ejer14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingresa un número entero positivo: ");
        int num = scanner.nextInt();
        int[] arreglo = new int[num];
        Random random = new Random();
        System.out.println("Arreglo generado: ");
        for (int i = 0; i < num; i++) {
            arreglo[i] = random.nextInt(101);
            System.out.print(arreglo[i] + "\t");  
        }

        int contadorpares = 0;
        int contadorimpares = 0;

        for (int i = 0; i < arreglo.length; i++) {
            if (arreglo[i] % 2 == 0) {
                contadorpares++;
            } else {
                contadorimpares++;  
            }
        }
        System.out.println("El número de pares es: " + contadorpares + " y el número de impares es: " + contadorimpares);
    }
}
