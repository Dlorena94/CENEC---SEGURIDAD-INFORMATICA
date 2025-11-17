
package tema1variables;

import java.util.Scanner;


   
public class EjercicioBucleMenu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean verdadfalso = false;
        int menu;

        System.out.println("Indica la opción: 1. Sumar 2. Restar 3. Multiplicar 4. Dividir 5. Salir");

        while (verdadfalso!=true) { 
        	

            if (menu == 5) {
                verdadfalso = true;
                System.out.println("Has elegido salir ");
           
            }else {
            	System.out.println("Has elegido otra opción ");
            	
            }
           
        }

        sc.close();
    }
}
