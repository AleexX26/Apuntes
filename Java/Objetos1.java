
public class Objetos1 {
    public static void main(String[] args) {

        /*
         * Declaro una variable objeto llamada frase
         * y con new String(); le digo que esa variable
         * va a contener un nuevo objeto de la case String
         * y ese objeto tiene en su interior una cadena
         * de caracteres que es "Soy una frase"
         */

        String frase = new String("Soy una frase.");

        // Ahora imprimo lo que contiene ese objeto frase
        System.out.println(frase);

        // ************************************************
        /*
         * Tambien podemos declarar un objeto String de la
         * siguiente manera
         */

        /*
         * Declaro un objeto de la clase string y lo almaceno
         * en la variable objeto llamada nombre
         */
        String nombre = new String();

        /*
         * Inicio la variable objeto nombre
         * con una cadena de caracteres
         */
        nombre = "Soy el contenido de la variable objeto nombre";

        // Imprimimos el contenido de la variable nombre.
        System.out.println(nombre);
    }
}