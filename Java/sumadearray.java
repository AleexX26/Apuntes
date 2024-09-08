import java.util.Random;

public class sumadearray {
    public static void main(String[] args) {
        int columna = 5;
        int filas = 5;
        Random random = new Random();
        int[][] matriz = new int[filas][columna];
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columna; j++) {
                matriz[i][j] = random.nextInt(101);
            }
        }
        int suma = matriz[0][0];
        double promedio = (double) suma / (filas* columna);
        double multiplicacion = matriz[0][0];
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columna; j++) {
                suma += matriz[i][j];
                multiplicacion *= matriz[i][j];
            }
        }
        System.out.println("Matriz: ");
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columna; j++) {
                System.out.print(matriz[i][j] + "\t");
            }System.out.println();
        }
        System.out.println("valor de la suma es: " + suma);
        System.out.println("Valor del promedio es: " + promedio);
        System.out.println("Valor de la multiplicaion es: " + multiplicacion);
    }
}
