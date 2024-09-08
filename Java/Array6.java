import java.util.Arrays;
public class Array6 {
    public static void main(String[] args) {
        int[] original = { 1, 2, 3, 4, 5, };
        int[] copia = new int[original.length];
        for (int i = 0; i < original.length; i++) {
            copia[i] = original[i];
        }
        System.out.println("Array original: " + Arrays.toString(original));
        System.out.println("Array copiado al reves:[ ");
        for (int i = copia.length - 1; i >= 0; i--) {
            System.out.print(copia[i]);
            if (i > 0) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}