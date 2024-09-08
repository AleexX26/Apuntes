public class coche {
    int km;
    String marca;
    String color;

    public static void main(String[] args) {
        coche coche1 = new coche();

        coche1.color = "rojo";
        coche1.marca = "audi";
        coche1.km = 100;

        System.out.println("El color del coche:" + coche1.color);
        System.out.println("El marca del coche:" + coche1.marca);
        System.out.println("El km del coche:" + coche1.km);

        coche coche2 = new coche();

        coche2.color = "azul";
        coche2.marca = "bmw";
        coche2.km = 10;

        System.out.println("El color del coche:" + coche2.color);
        System.out.println("El marca del coche:" + coche2.marca);
        System.out.println("El km del coche:" + coche2.km);
    }
}
