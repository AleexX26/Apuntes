
import java.util.Scanner;
public class Ejer15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner (System.in);
        System.out.println("Dime la cantidad de calificaciones que quieres realizar");
        int cantidad = scanner.nextInt();
        int num= cantidad;
        for (int i = 0; i < cantidad; i++) {
            System.out.println("Ingrese la cantidad " +num);
            int calificaciones = scanner.nextInt();
        }
    }
}