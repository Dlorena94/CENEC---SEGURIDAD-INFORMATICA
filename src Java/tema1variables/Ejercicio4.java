package tema1variables;

public class Ejercicio4 {

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        float importe, iva, total;
        importe = 123.40f;
        iva = 0.21f;
        total = importe * iva;

        System.out.printf("El importe es %.2f%n", total);
       System.out.println("********************");
    /*
     * %: Indica el inicio de una especificación de formato.
.2: Especifica la cantidad de decimales que se mostrarán. En este caso, 2 decimales.
f: Indica que el valor será formateado como un número de punto flotante.
%n: Representa un salto de línea. Es una forma portable de agregar una nueva línea en diferentes sistemas operativos.
      */  
    }
}