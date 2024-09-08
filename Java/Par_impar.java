import java.util.Scanner;

public class Par_impar {
    static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num;
        System.out.println("Dime um número: ");
        num = sc.nextInt();
        if (num % 2 == 0) {
            System.out.println(num + " Es par");
        } else {
            System.out.println(num + " Es impar");
        }
    }
}