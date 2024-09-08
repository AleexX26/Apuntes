
public class Array2 {
    public static void main(String[] args) {
        int[] numeros = { 15, 2, 23, 8, 4, 10 };
        int maximo = numeros[0];
        int maximo2 = numeros[1];
        for (int i = 2; i < numeros.length; i++) {
            if (numeros[i] > maximo) {
                maximo2 = maximo;
                maximo = numeros[i];
            }
            if (numeros[i] > maximo2 && numeros[i] != maximo) {
                maximo2 = numeros[i];
            }
        }
        System.out.println("el valor maximo: " + maximo + " y " + maximo2);
    }
}