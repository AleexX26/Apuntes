import javax.swing.JOptionPane;

public class lista {
    public static void main(String[] args) {

        boolean finalizar = false;

        String[] nombres = new String[100];
        double[] precios = new double[100];
        int[] cantidadDeProducto = new int[100];

        int i = -1;

        while (finalizar != true) {

            System.out.println("== GESTION DE INVENTARIO SIMPLE ==");
            System.out.println("1.Agregar un producto");
            System.out.println("2.Mostrar lista de productos");
            System.out.println("3.Salir");
            String text = JOptionPane.showInputDialog("Seleccione una opción");
            int opcion = Integer.parseInt(text);

            switch (opcion) {

                case 1:
                    i++;

                    String nombre = JOptionPane.showInputDialog("Inserte nombre de producto");

                    String precioText = JOptionPane.showInputDialog("Inserte precio de producto");
                    double precio = Double.parseDouble(precioText);

                    String cantidadText = JOptionPane.showInputDialog("Inserte cantidad de producto");
                    int cantidad = Integer.parseInt(cantidadText);

                    nombres[i] = nombre;
                    precios[i] = precio;
                    cantidadDeProducto[i] = cantidad;
                    break;
                case 2:
                    for (int j = 0; j < 5; j++) {

                        System.out.println("== LISTA PRODUCTOS ==");
                        System.out.println("== PRODUCTO " + (j + 1));
                        System.out.println("Nombre: " + nombres[j]);
                        System.out.println("Cantidad: " + cantidadDeProducto[j]);
                        System.out.println("Precio por unidad: " + precios[j]);
                        System.out.println(" ");

                        JOptionPane.showMessageDialog(null, "== LISTA PRODUCTOS ==" + "\n" + "== PRODUCTO " + (j + 1)
                                + "== " + "\n" + "Nombre: " + nombres[j] + "\n" +
                                "Cantidad: " + cantidadDeProducto[j] + "\n" + "Precio por unidad: " + precios[j]);

                    }
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null, "El programa se cerrará");
                    finalizar = true;
                    System.exit(0);
                    break;

                default:
                    JOptionPane.showMessageDialog(null, "Inserte una opción válida entre 1 y 3");
                    break;
            }
        }
    }
}
