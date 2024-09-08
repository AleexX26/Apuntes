import java.util.Random;

public class Ejer12 {
    public static void main(String[] args) {
        Random random = new Random(); //Vamos a pedirle que nos ponga numeros randoms
        int filas = 5; //Delcaramos la variable fila hasta un maximo de 5
        int columnas = 5; // Delcaramos la variable columna hasta un maximo de 5
        int[][] matriz = new int[filas][columnas]; // Aqui esta haciendo la matriz bidimensional 
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                matriz[i][j] = random.nextInt(101); // 
            }
        }
        int suma = matriz[0][0];
        double promedio = (double) suma / (filas* columnas);
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                suma += matriz[i][j];
            }
        }
        int maximo = matriz[0][0];
        int filamaximo = 0;
        int columnamaximo = 0;
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (matriz[i][j] > maximo) {
                    maximo = matriz[i][j];
                    filamaximo = i;
                    columnamaximo = j;
                }
            }
        }
        int minimo = matriz[0][0];
        int filaminimo = 0;
        int columnaminimo = 0;
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (matriz[i][j] < minimo) {
                    minimo = matriz[i][j];
                    filaminimo = i;
                    columnaminimo = j;
                }
            }
        }
        System.out.println("La matriz es: ");
        for (int i = 0 ; i < filas; i++) {
            for (int j = 0 ; j < filas; j++) {
                System.out.print(matriz[i][j]+ "\t");
            }System.out.println();
        }   
        System.out.println("El minimo es: " + minimo + " el maximo es: " + maximo);
        System.out.println("El ressultado de la suma es: " + suma);
        System.out.println("El ressultado del promedio es: " + promedio);
    }
}

