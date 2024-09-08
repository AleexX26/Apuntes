import java.util.Random;

public class Ejer10 {
    public static void main(String[] args) {
        Random random = new Random();
        int filas = 5;
        int columnas = 5;
        int[][] matriz = new int[filas][columnas];
        int suma = matriz[0][0];
        int maximo = matriz[0][0];
        int filamaximo = 0;
        int columnamaximo = 0;
        int minimo = matriz[0][0];
        int filaminimo = 0;
        int columnaminimo = 0;
        System.out.println("La matriz es: ");
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                matriz[i][j] = random.nextInt(101);
                System.out.print(matriz[i][j] + "\t");
                suma += matriz[i][j];
                if (matriz[i][j] > maximo) {
                    maximo = matriz[i][j];
                    filamaximo = i;
                    columnamaximo = j;
                }
                if (matriz[i][j] < minimo) {
                    minimo = matriz[i][j];
                    filaminimo = i;
                    columnaminimo = j;
                }
            }
            System.out.println();
        }
        double promedio = (double) suma / (filas * columnas);
        System.out.println("El minimo es: " + minimo + " el maximo es: " + maximo);
        System.out.println("El ressultado de la suma es: " + suma);
        System.out.println("El ressultado del promedio es: " + promedio);
    }
}
