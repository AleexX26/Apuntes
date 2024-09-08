import java.util.Random;

public class minimodearray {
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
        int minimo = matriz[0][0];
        int filaminimo = 0;
        
        int columnaminimo = 0;
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columna; j++) {
                if (matriz[i][j] < minimo) {
                    minimo = matriz[i][j];
                    filaminimo = i;
                    columnaminimo = j;
                }
            }
        }
        System.out.println("Matriz: ");
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columna; j++) {
                System.out.print(matriz[i][j] + "\t");
            }System.out.println();
        }
        System.out.println("valor minimo: " + minimo);
        System.out.println("Posicion del minimo: " + filaminimo + "," + columnaminimo);
    }
}
