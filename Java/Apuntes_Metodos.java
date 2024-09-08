/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cursojava;

/**
 *
 * @author minis
 */
public class Apuntes_Metodos {
   
/*
 * Método = Un método es una acción o comportamiento de los objetos
 * Parámetro = Son para la declaración de los métodos
 * Argumentos son para la invocación de los métodos
 * Método "void" no retona nada
 * Método "Int" nos retorna la función a realizar
 * Método String" Nos retorna una cadena (Caracteres)
 */ 
    

/*El método  𝑚𝑎𝑖𝑛(), tiene que estar declarado dentro de una clase.

𝑝𝑢𝑏𝑙𝑖𝑐 : cada método en una clase puede ser público, protegido o privado dependiendo del nivel de acceso que el programador 
quiere darle. “ 𝑝𝑢𝑏𝑙𝑖𝑐 ” significa que el método puede ser accedido desde cualquier otro método que tenga una instancia de 
esta clase, “ 𝑝𝑟𝑜𝑡𝑒𝑐𝑡𝑒𝑑 ” quiere decir que el método sólo puede ser accedido desde dentro de la misma clase y desde clases 
derivadas de la clase donde se ha declarado y “ 𝑝𝑟𝑖𝑣𝑎𝑡𝑒 ” quiere decir que el método sólo puede ser accedido desde dentro de 
la misma clase.
    
𝑠𝑡𝑎𝑡𝑖𝑐 : un método puede ser de instancia o de clase. Un método NO estático es un método de instancia (que necesita una instancia 
de la clase donde se declara para ser invocado) y un método estático es un método de clase (sólo se necesita invocarlo dada la 
clase, no un objeto de dicha clase).
    
𝑣𝑜𝑖𝑑 : Los métodos pueden devolver algo, por ejemplo, un método que suma dos números, devuelve el resultado de la suma; pero 
hay métodos que no devuelven nada y que sólo ejecutan acciones. Dichos métodos se declaran con la palabra reservada “ 𝑣𝑜𝑖𝑑 ” 
(vacío) como tipo de retorno.
    
𝑚𝑎𝑖𝑛 : Es el nombre del método que la máquina virtual de Java busca para comenzar a ejecutar un programa. Todos los métodos 
tienen un nombre.
    
𝑆𝑡𝑟𝑖𝑛𝑔 : Es una clase que define cadenas de caracteres. Gracias a la clase String, Java puede manipular textos.  
𝑆𝑡𝑟𝑖𝑛𝑔𝑠=“𝐻𝑜𝑙𝑎𝑚𝑢𝑛𝑑𝑜” define una cadena.
    
𝑆𝑡𝑟𝑖𝑛𝑔 []: Cualquier clase que se declara con corchetes “[]”, quiere decir que lo que tienes no es una instancia de esa clase, 
sino un array de objetos de dicha clase. Ejemplo: 𝑆𝑡𝑟𝑖𝑛𝑔[]𝑚𝑒𝑠𝑒𝑠; contendría los nombres de los meses del año. El método main() 
de Java necesita un String[] porque el usuario de nuestro programa puede pasar parámetros extra desde la línea de comando a 
nuestro programa. Esos parámetros, el programador los recibe a través de ese array.
     
     */
 //Metodo principal, en este caso no hemos llamado a ningún metodo, no hay nada dentro de las llaves solo imprimir

    void Hola() {
        
        
//System.out.print("Hola Mundo");//debemos acabar con ;
        System.out.println("Hola Mundo");//imprime el texto especificado dentro de los paréntesis en la pantalla  ;

    }

    
     /*Definición de propiedades--> Caracterírticas del elemento que describimos con la clase
      Definición de los métodos--> Comportamiento y funcionalidades del elemento
     */
    public static void main(String[] args) {
        // Función principal, todo el código empezará desde el main
        Apuntes_Metodos objeto = new Apuntes_Metodos();
        objeto.Hola();

    }
}
