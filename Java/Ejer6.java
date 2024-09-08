import java.util.Scanner;
public class Ejer6{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] gastosSemana = new double[7];
        double totalGastos = 0; 
        System.out.println("registro de Gastos Diarios");
        System.out.println("Ingresa tusgastos diarios durante la semana: ");
        for (int i = 0; i < gastosSemana.length; i++){
            System.out.println("Dia " + (i + 1) + ": $");
            gastosSemana[i] = sc.nextDouble();
            totalGastos += gastosSemana[i];
        }
        double promedioGastos = totalGastos / 7;
        System.out.println(" \nresumen de gastos: ");
        System.out.println(" Gastos total de la semana: $" + totalGastos);
        System.out.println("Gastos promedio por dia: $" + promedioGastos);

        sc.close(); 
    }
}