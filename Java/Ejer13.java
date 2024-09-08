import java.util.Scanner;
public class Ejer13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Dime un numero");
        int cantidad = scanner.nextInt();
        int num = 0;
        int suma = 0;
        for (int i = 0; i < cantidad; i++) {
            num++;
            System.out.println("Ingrese la nota " + num);
            int calificacion = scanner.nextInt();
            suma += calificacion;
        }
        double promedio = (double) suma / cantidad;
        System.out.println("El promedio " + promedio);
        if (promedio >= 6) {
            System.out.println("Aprobado");
        } else {
            System.out.println("Suspenso");
        }
    }
}