import java.util.Arrays;
public class Array5 {
    public static void main(String[] args) {
        int[] original = { 1, 2, 3, 4, 5 };
        int[] copia = new int[original.length];
        for (int i = 0; i < original.length; i++) {
            copia[i] = original[i];
        }
        System.out.println("Array original: " + Arrays.toString(original));
        System.out.println("Array copiado: " + Arrays.toString(copia));
    }
}
