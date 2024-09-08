import java.util.Scanner;
public class area_circulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dime el area del circulo");
        double radio = sc.nextDouble();
        double p = 3.1415;
        double area = p * radio * radio;
        System.out.println("El area del circulo es: " + area);
    }
}
