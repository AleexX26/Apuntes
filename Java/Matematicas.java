import java.util.Scanner; //Importamos una biblioteca para que el usuario introduca un dato
//En una ecuacion de segundo grado tenemos A, b y c

public class Matematicas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // La llamamo y la ponemos un nombre, por ejemplo la hemos lladao sc

        // Aqui hemos puesto todas las variables de tipo decima
        double a;
        double b;
        double c;
        double x1;
        double x2;
        double raiz_cuadrada;

        // Hemos puesto que diga que ponga un valor a cada letra
        System.out.println("Introduce el valor de a: ");
        a = sc.nextDouble();
        System.out.println("Introduce el valor de b: ");
        b = sc.nextDouble();
        System.out.println("Introduce el valor de c: ");
        c = sc.nextDouble();

        // Se realizara la raiz cuadrada, ya que no existe ningun caracter que sea para
        // hacer la raiz cuadrada
        raiz_cuadrada = (b * b - 4 * a * c);
        System.out.println("La raiz cuadrada es = " + raiz_cuadrada);
        /*
         * Esto sirve para saber si tiene soluciones:
         * -> Si al hacer la raiz cuadrada da menos que 0 no existen soluciones
         * -> Si el resultado de la raiz cuadrada es igual a 0 no es una ecuacion de
         * segundo grado
         * -> Si el resultado de la raiz cudrada no es igual o menor que 0 va a calular
         * -b +- el resultado de la raiz cuadrada
         */
        if (raiz_cuadrada < 0) {
            System.out.println("No existen soluciones reales");
        } else {
            if (a == 0) {
                System.out.println("No es una ecuacion de segundo grado");
            } else {
                x1 = (-b + Math.sqrt(raiz_cuadrada)) / (2 * a);
                x2 = (-b - Math.sqrt(raiz_cuadrada)) / (2 * a);

                System.out.println("Solucion 1 = " + x1);
                System.out.println("Solucion 2 = " + x2);
            }
        }
    }
}
