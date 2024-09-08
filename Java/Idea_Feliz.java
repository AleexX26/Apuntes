
import java.util.Scanner;

public class Idea_Feliz {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Inserta lo que sea");
        int nose = sc.nextInt();
        int euros = 0;

        if (nose > 100) {
            euros = 65;
            System.out.println("El precio es: " + euros);
        } else if (nose >= 50) {
            euros = 70;
            System.out.println("El precio es: " + euros);
        } else if (nose >= 30) {
            euros = 80;
            System.out.println("El precio es: " + euros);
        } else {
            if (nose > 0) {
                euros = 6000 / nose;
                System.out.println("El precio es: " + euros);
            } else {
                System.out.println("El número debe ser mayor que 0 para calcular el precio.");
            }
        }

        sc.close();
    }
}
