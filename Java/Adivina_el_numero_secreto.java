import java.util.Scanner;

public class Adivina_el_numero_secreto {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero, i= 0;
        int numerosecreto = (int) (Math.random() * 100 + 1);
        while (i <= 100) {
            i = i + 1;
            System.out.println("Que numero crees que es del 1 al 100, va a ser numero aleatorio");
            numero = sc.nextInt();
            if (numero > numerosecreto) {
                System.out.println("el numero es mas bajo");
            } else if (numero < numerosecreto) {
                System.out.println("el numero es mas alto");
            } else if (numero == numerosecreto) {
                System.out.println("el numero es el correcto");
                break;
            }
        }
    }
}
