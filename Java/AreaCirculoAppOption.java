import javax.swing.JOptionPane;

public class AreaCirculoAppOption {
    public static void main(String[] args) {
        String texto = JOptionPane.showInputDialog("Ingrese un Radio: ");
        
        double radio = Double.parseDouble(texto);
        double area = Math.PI * Math.pow(radio, 2);
        System.out.println("El area del circulo es: " + area + " cm^2");

    }
    
}
