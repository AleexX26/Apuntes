public class Ejer11 {
    public static void main(String[] args) {
        int [] numeros={23,45,12,67,9,56,31,8,72,15};
        int maximo = 0;
        int maximo2 =1;
        for (int i = 2; i < numeros.length; i++) {
            if (numeros[i] > maximo) {
                maximo2 = maximo;
                maximo = numeros[i];
            }
            if (numeros[i] > maximo2 && numeros[i] != maximo) {
                maximo2 = numeros[i];
            }
        }
        System.out.println(" El primer numero mayor es: " + maximo + " y el segundo es: " + maximo2);
    }
}
