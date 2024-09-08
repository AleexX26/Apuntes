import java.util.Scanner;

public class Ejer7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(
                System.in);

        // Inicializamos variables para el promedio y el contador de aprobados
        double promedio = 0;
        int aprobados = 0;
        int reprobados = 0;

        // Pedimos al usuario que ingrese la cantidad de estudiantes
        System.out.print("Ingrese la cantidad de estudiantes: ");
        int numEstudiantes = scanner.nextInt();

        // Iteramos sobre cada estudiante
        for (int i = 1; i <= numEstudiantes; i++) {
            // Pedimos al usuario que ingrese la calificación del estudiante actual
            System.out.print("Ingrese la calificacion del estudiante " + i + ": ");
            double calificacion = scanner.nextDouble();

            // Sumamos la calificación al promedio
            promedio += calificacion;

            // Verificamos si el estudiante aprobó o reprobó
            if (calificacion >= 5) {
                aprobados++;
            } else {
                reprobados++;
            }
        }

        // Calculamos el promedio dividiendo la suma de calificaciones por el número de
        // estudiantes
        promedio /= numEstudiantes;

        // Mostramos los resultados
        System.out.println("El promedio de calificaciones es: " + promedio);
        System.out.println(aprobados + " estudiantes aprobaron.");
        System.out.println(reprobados + " estudiantes reprobaron.");

        scanner.close();
    }
}