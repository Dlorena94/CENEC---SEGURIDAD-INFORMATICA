package tema1variables;

import java.util.Scanner;

public class BucleDoWhile1 {
    public static void main (String[] args) {
    	Scanner scanner = new Scanner(System.in);
    	System.out.print("Introduce el número para ver su tabla de multiplicar (1-10): ");
    	int numero = scanner.nextInt();
    	scanner.close();
    	System.out.println("--- Tabla de multiplicar del " + numero + " ---");

        int i = 1;
        do {
			System.out.println(numero+ "x" +1+ "=" +i*numero);
			i++;
		} while (i <= 10);
    }

}
