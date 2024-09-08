import java.util.Scanner;
public class Ejer8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dime el precio del producto");
        double precio= sc.nextDouble();
        System.out.println(" Dime el descuento");
        double descuento= sc.nextDouble();
        double preciodescuento = (precio*descuento) / (100);
        double precio2 = (precio - preciodescuento);
        System.out.println(" el precio es " + precio + " el descuento " + descuento + " con el descuento es: "+ precio2);

    }
}
