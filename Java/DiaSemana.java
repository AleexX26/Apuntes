import java.util.Scanner;
public class DiaSemana {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese una dia de la semana del 1 al 7, teniendo en cuenta que el 1 es el Lunes y el 7 el Domingo: ");
        int DiaSemana = sc.nextInt();

        switch (DiaSemana) {
            case 1 ->
                System.out.println("Lunes");
            case 2 ->
                System.out.println("Martes");
            case 3 ->
                System.out.println("Miercoles");
            case 4 ->
                System.out.println("Jueves");
            case 5 ->
                System.out.println("Viernes");
            case 6 ->
                System.out.println("Sabado");
            case 7 ->
                System.out.println("Domingo");
            default ->
                System.out.println("Invalido, intentelo otra vez");
        }
    }
}