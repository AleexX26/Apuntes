public class Aray3 {
    public static void main(String[] args) {
        int[] numeros = { 15, 2, 8, 4, 10 };
        int minimo = numeros[2];
        int maximo = numeros[2];
        for (int i = 2; i < numeros.length; i++) {
            if (numeros[i] < minimo) {
                minimo = numeros[i];
            }
            if (numeros[i] > maximo) {
                maximo = numeros[i];
            }
        }
        System.out.println("el valor maximo: " + minimo);
        System.out.println("el valor maximo: " + maximo);
    }
}
