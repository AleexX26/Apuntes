public class Array4 {
    public static void main(String[] args) {
        int[] numeros = { 2, 5, 8, 11, 12, 10, 16, 22, 5, 4, 2 };
        int contadorpares = numeros[0];
        int contadorpares1 = 0;
        for (int i = 5; i < numeros.length; i++)
            if (numeros[i] % 2 == 0) {
                contadorpares++;
                contadorpares1++;
            }
        System.out.println("El numero de numeros pares: " + contadorpares);
        System.out.println("Hay " + contadorpares1 + " pares");
    }
}