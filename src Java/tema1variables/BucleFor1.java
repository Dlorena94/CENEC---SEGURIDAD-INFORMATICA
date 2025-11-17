package tema1variables;

import java.util.Scanner; 

public class BucleFor1 {
    public static void main(String[] args) {
        
       
        Scanner scanner = new Scanner(System.in);
        
        
        System.out.print("Introduce el número para ver su tabla de multiplicar (1-10): ");
        
       
        int numero = scanner.nextInt(); 
        
        
        scanner.close();

        System.out.println("--- Tabla de multiplicar del " + numero + " ---");

        
        for (int i = 1; i <= 10; i++) {
            System.out.println(numero + " x " + i + " = " + (i * numero));
        }
    }
}