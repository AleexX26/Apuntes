
import javax.swing.JOptionPane;
public class Calculadora {
    public static void main(String[] args) {
        double  num1;
        double  num2;
        double  resultado = 0;

        String texto = JOptionPane.showInputDialog("Digite o primeiro número: ");
        num1 = Integer.parseInt(texto);
        
        String operation = JOptionPane.showInputDialog( "Digite la operacion: ");

        String texto2 = JOptionPane.showInputDialog("Digite o segundo número: ");
        num2 = Integer.parseInt(texto2);

        switch (operation){
            case "+":
                resultado = num1 + num2;
                break;
            case "-":
                resultado = num1 - num2;
                break;
            case "*":
                resultado = num1 * num2;
                break;
            case "/":
                resultado = num1 / num2;
                break;
        }
        JOptionPane.showMessageDialog(null, num1+ "" +operation+ "" + num2+ "= " + resultado);
    }
}
