import java.util.Scanner;

public class Ejer5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        String nombre_alumno;
        double evaluacion1;
        double evaluacion2;
        double evaluacion3;
        double evaluacion_final;

        System.out.println("Nombre alumno: ");
        nombre_alumno = entrada.nextLine();

        System.out.println("Nota primera evaluación: ");
        evaluacion1 = entrada.nextDouble();

        System.out.println("Nota segunda evaluación: ");
        evaluacion2 = entrada.nextDouble();

        System.out.println("Nota tercera evaluación: ");
        evaluacion3 = entrada.nextDouble();

        evaluacion_final = (evaluacion1 + evaluacion2 + evaluacion3) / 3;

        System.out.println("El nombre del alumno es " + nombre_alumno + " y su media es " + evaluacion_final);
    }
}