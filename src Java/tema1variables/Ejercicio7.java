package tema1variables;

import java.util.Scanner;

public class Ejercicio7 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Introduce el importe: ");
        double importe = sc.nextDouble();
        
        System.out.print("Introduce el IVA (en porcentaje, por ejemplo, 21 para 21%): ");
        double ivaPorcentaje = sc.nextDouble();
        
        double iva = ivaPorcentaje / 100;
        double total = importe * iva;
        
        System.out.printf("El importe del IVA es %.2f%n", total);
        
        /*
         * %: Indica el inicio de una especificación de formato.
         * .2: Especifica la cantidad de decimales que se mostrarán. En este caso, 2 decimales.
         * f: Indica que el valor será formateado como un número de punto flotante.
         * %n: Representa un salto de línea. Es una forma portable de agregar una nueva línea en diferentes sistemas operativos.
         */
        
        sc.close();
    }
}
