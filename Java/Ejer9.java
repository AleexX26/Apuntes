public class Ejer9 {
    public static void main(String[] args) {
        int numero[] = { 9, 2, 3, 4, 6 };
        int maximo = numero[0];
        int minimo = numero[0];
        int suma;
        int contadorpares = numero[0];
        int contadorpares1 = 0;
        for (int i = 2; i < numero.length; i++) {
            if (numero[i] > maximo) {
                maximo = numero[i];
            }
            if (numero[i] < minimo) {
                minimo = numero[i];
            }
            for (int j = 1; i < numero.length; i++) {
                if (numero[j] % 2 == 0) {
                    contadorpares++;
                    contadorpares1++;
                }
            }
            suma = minimo + maximo;
            System.out.println("El valor de maximo: " + maximo + " el valor minimo: " + minimo);
            System.out.println("El numero de pares: " + contadorpares);
            System.out.println("Hay " + contadorpares1 + " pares");
            System.out.println("El valor de la suma: " + suma);
        }
    }
}
