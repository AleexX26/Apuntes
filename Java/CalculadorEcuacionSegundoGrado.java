import java.util.Scanner;

public class CalculadorEcuacionSegundoGrado {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a;
        double b;
        double c;
        double x1;
        double x2;
        double d;

        System.out.println("Introduce el valor de a: ");
        a = sc.nextDouble();
        System.out.println("Introduce el valor de b: ");
        b = sc.nextDouble();
        System.out.println("Introduce el valor de c: ");
        c = sc.nextDouble();

        d = (b * b) - (4 * a * c);
        if (d < 0) {
            System.out.println("No existen soluciones reales");
        } else if (a == 0) {
            System.out.println("No es una ecuacion de primer grado");
        } else {
            x1 = (-b + Math.sqrt(d)) / (2 * a);
            x2 = (-b - Math.sqrt(d)) / (2 * a);
            System.out.println("Solucion1= " + x1);
            System.out.println("Solucion2 = " + x2);
        }
    }
}
