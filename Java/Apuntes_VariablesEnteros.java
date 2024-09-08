
package cursojava;

/**
 *
 * @author minis
 */
/*VARIABLES PRIMITIVAS
Una Variable es un espacio de memoria que almacena un valor, es decir como si tuvieramos una caja y guardamos algo*/

public class Apuntes_VariablesEnteros {
    
        public static void main(String[] args) {
        // Función principal, todo el código empezará desde el main
        
        /*byte es una variable en este caso entero, almacena datos de números enteros. Esta variable "byte va del número 
        -128 a 127. Qué quiere decir esto, que si ponemos en variable entero el número 130 no lo reconocería*/
        
        byte entero ;
        entero = 1;
       
        //También podemos hacerlo de esta forma "byte entero = 1";

        System.out.println("Entero: "+entero);//sale por pantalla Entero + el valor de la variable

        
        /*Variable tipo short en este caso entero, almacena datos de números enteros. Esta variable "byte va del número 
        -32.768 a 32.767. Qué quiere decir esto, que si ponemos en variable entero el número 33000 no lo reconocería
        
        short entero;
        entero = 11000;
        
        //También podemos hacerlo de esta forma "short entero = 11000";

        System.out.println("Entero: "+entero);//sale por pantalla Entero + el valor de la variable
        */
        
        
        
        /*Variable tipo Int en este caso entero (es el más utilizado), almacena datos de números enteros. 
        Esta variable "int va del número -2.147.483.648 a 2.147.483.647. Qué quiere decir esto, que si ponemos en variable entero el número 3.000.000.000 no lo reconocería
        
        int entero;
        entero = 2000000000;
        
        //También podemos hacerlo de esta forma "int entero = 1";

        System.out.println("Entero: "+entero);//sale por pantalla Entero + el valor de la variable
        */
        
        
        /*Variable tipo long en este caso entero, almacena datos de números enteros. 
        Esta variable "int va del número -9.223.372.036.854.775.808 a 9.223.372.854.775.807 
        Qué quiere decir esto, que si ponemos en variable entero el número 3.000.000.000 no lo reconocería
        
        long entero;
        entero = 2000000000000000000;
        
        //También podemos hacerlo de esta forma "int entero = 1";

        System.out.println("Entero: "+entero);//sale por pantalla Entero + el valor de la variable
        */
        
        //OJO SOLO SE PUEDEN PONER NÚMEROS ENTEROS, NO SE PUEDE PONER NÚMEROS CON DECIMALES.
        }
        } 