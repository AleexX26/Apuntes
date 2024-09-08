import javax.swing.JOptionPane;
public class tabla2 {
    public static void main(String[] args) {
        String texto = JOptionPane.showInputDialog(" dime un numero");
        int numero= Integer.parseInt(texto);
        for (int i = 1; i <= 10; i++) {
            int resultado = numero *i;
            System.out.println(numero + "x" + i + " = " + resultado);
        }
    }
}