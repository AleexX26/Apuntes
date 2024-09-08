import java.util.Scanner;
public class Ejer4 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Que quieres para comer, (1)hamburguesa, (2)pizza");
        int  leer1 =leer.nextInt();
        if(leer1 == 1 ){
            System.out.println("has elegido una Hamburguesa de Angus al punto(la vaca chillando)");
        } else if(leer1 == 2){
            System.out.println("Has elegido un Pizza con Piña ");
        }else {
            System.out.println("Error");
        }
    }
}
