package tema1variables;

import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Introduce tu nombre: ");
        String nombre = sc.nextLine();
        
        System.out.print("Introduce tus apellidos: ");
        String apellidos = sc.nextLine();
        
        System.out.println("Bienvenida " + nombre + " " + apellidos);
        
        sc.close();
    }
}
